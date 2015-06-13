'''
Created on Jun 3, 2015

@author: haidong
'''
import unittest
from ocef.bouncedEmails import BouncedEmails


class Test(unittest.TestCase):

    def testGetEmailsInDirectory(self):
        bouncedEmails = BouncedEmails('/home/haidong/ocef/data')
        bouncedEmails.getAllEmails()
        self.assertEqual(len(bouncedEmails.allEmailFiles), 6483)

    def testFirstEmailFile(self):
        bouncedEmails = BouncedEmails('/home/haidong/ocef/data')
        bouncedEmails.getAllEmails()
        self.assertIn('/home/haidong/ocef/data/1420033341.M103906P22128.ocef.org,S=38925,W=40053:2,S', bouncedEmails.allEmailFiles)

    def testFinalRecipient1(self):
        bouncedEmails = BouncedEmails('/home/haidong/ocef/data')
        bouncedEmails.getAllEmails()
        pass

    def testGetEmail(self):
        bouncedEmails = BouncedEmails('/home/haidong/ocef/data')
        bouncedEmails.getAllEmails()
        em = bouncedEmails.getEmail('/home/haidong/ocef/data/1420033341.M103906P22128.ocef.org,S=38925,W=40053:2,S')
        self.assertEqual(em.get_content_maintype(), 'multipart')

    def testGetEmailAddressAndDiagCode(self):
        bouncedEmails = BouncedEmails('/home/haidong/ocef/data')
        bouncedEmails.getAllEmails()
        em = bouncedEmails.getEmail('/home/haidong/ocef/data/1420033341.M103906P22128.ocef.org,S=38925,W=40053:2,S')
        em_add, diagCode = '1036546290@qq.com', 'smtp; 550 Mail content denied.    http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=20022&&no=1000726' 
        self.assertEqual(bouncedEmails.getEmailAddrAndDiagCode(em), (em_add, diagCode))
    
    def testOutputFile(self):
        bouncedEmails = BouncedEmails('/home/haidong/ocef/data')
        bouncedEmails.getAllEmails()
        bouncedEmails.outputEmailAddrAndDiagCode('/home/haidong/ocef/parsingResult.csv')
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()