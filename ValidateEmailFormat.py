'''
Created on Feb 16, 2019
Validate Email Format using regular expression
https://docs.oracle.com/cd/E19683-01/817-0204/6mg168c5t/index.html
https://www.mailboxvalidator.com/resources/articles/acceptable-email-address-syntax-rfc/
@author: rduvalwa2
'''
import re

class verifyEmailFormat:
    
        def __init__(self,em):
            self.eAddress = em
            print(self.eAddress)
            
        def verifyAt(self):
            if "@" in self.eAddress:
                return True
            else:
                return False
                
        def verifyDomain(self):
            result = False
            domainTypeList = [".com",".org",".edu",".gov",".mil",".net"]
            for domain in domainTypeList:
                print("domain is ", domain)
                if domain in self.eAddress: 
                    #mtch = re.match(domain, self.eAddress)
                    #print("mtch is ",mtch)
                    print("email is ", self.eAddress)
                    result = True
            return result
                       
        def verfiyLocalName(self):
            splitE = self.eAddress.split('@')
            print("split is ",splitE)
            print("local lenth is ", len(splitE[0]))
            if len(splitE[0]) < 65:
                return True
            else:
                return False
            
        def verifyFormat(self):
            result = False
            allResults = [self.verfiyLocalName(), self.verifyDomain(), self.verifyAt()]
            print(allResults)
            if False not in allResults:
                return True
            
            
                
if __name__ == "__main__":
    import unittest
    
    class TestVerifyEmailFormat(unittest.TestCase):

        def setUp(self):
            self.eMail = "reddog@gamil.com"
            self.vEm = verifyEmailFormat(self.eMail)
            
        def test_verifyAt(self):     
            print("at test is " ,self.vEm.verifyAt())
            self.assertTrue(self.vEm.verifyAt())
            
        def testDomainPass(self):
            eMail = "reddog@gamil.com"
            v = verifyEmailFormat(eMail)
            print("pass domain test is ", v.verifyDomain())
            self.assertTrue(v.verifyDomain())
            
        def testDomainFail(self):
            eMail = "reddog@gamil.moc"
            v = verifyEmailFormat(eMail)
            print("fail domain test is ", v.verifyDomain())
            self.assertFalse(v.verifyDomain())

        def testLocal(self):
            #  v = verifyEmailFormat(eMail)
            self.assertTrue(self.vEm.verfiyLocalName())
            
        def testVerifyFormatPass(self):
            self.assertTrue(self.vEm.verifyFormat())
                      
        def testVerifyFormatFail(self):
            eMail = "reddoggamil.com"
            v = verifyEmailFormat(eMail)
            self.assertFalse(v.verifyFormat())
    
    unittest.main()