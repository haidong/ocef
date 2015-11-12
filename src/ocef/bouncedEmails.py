import os
import email


class BouncedEmails(object):
    """Find out donor's invalid email addresses for OCEF. Given a directory
    where all bounced email message are stored, produce a tab-delimited file
    with invalid email address and the reason it cannot be delivered. All
    email file in directory conform to RFC 822"""

    def __init__(self, sourceDirectory):
        """Initialize sourceDirectory, under which all returned email is
        stored"""
        self.sourceDirectory = sourceDirectory
        self.allEmailFiles = []

    def getAllEmails(self):
        """Produce a list of all email files with full path"""
        for root, directories, filenames in os.walk(self.sourceDirectory):
            for filename in filenames:
                self.allEmailFiles.append(os.path.join(root, filename))

    def getEmail(self, fileName):
        """Given email file name, return a email.message object"""
        f = open(fileName, 'r')
        return email.message_from_file(f)

    def getEmailAddrAndDiagCode(self, em):
        """Given email message, return email address and delivery failure
        diagnostic code. Here I use some magic list indexing. Need to refactor
        to avoid the magic index down the road"""
        for part in em.walk():
            if part.get_content_type() == 'message/delivery-status':
                y = part.get_payload()[1]
                emailAddress = y.get_all('Final-Recipient')[0].split(';')[1].strip()
                try:
                    diagCode = y.get_all('Diagnostic-Code')[0].replace('\n', '')
                except IndexError:
                    diagCode = 'N/A'
                return emailAddress, diagCode

    def outputEmailAddrAndDiagCode(self, outputFile):
        f = open(outputFile, 'w')
        for em in self.allEmailFiles:
            emObj = self.getEmail(em)
            try:
                emailAddress, diagCode = self.getEmailAddrAndDiagCode(emObj)
                f.write(emailAddress + '\t' + diagCode + '\n')
            except:
                pass
                #f.write(em + '\n')
