import unittest

import swot

class TestSwot(unittest.TestCase):
    def test_swot(self):
        self.assertTrue(swot.is_academic("lreilly@stanford.edu"))          
        self.assertTrue(swot.is_academic("LREILLY@STANFORD.EDU"))          
        self.assertTrue(swot.is_academic("Lreilly@Stanford.Edu"))          
        self.assertTrue(swot.is_academic("lreilly@slac.stanford.edu"))     
        self.assertTrue(swot.is_academic("lreilly@strath.ac.uk"))          
        self.assertTrue(swot.is_academic("lreilly@soft-eng.strath.ac.uk")) 
        self.assertTrue(swot.is_academic("lee@ugr.es"))                    
        self.assertTrue(swot.is_academic("lee@uottawa.ca"))                
        self.assertTrue(swot.is_academic("lee@mother.edu.ru"))             
        self.assertTrue(swot.is_academic("lee@ucy.ac.cy"))                 
        self.assertFalse(swot.is_academic("lee@leerilly.net"))              
        self.assertFalse(swot.is_academic("lee@gmail.com"))                 
        self.assertFalse(swot.is_academic("lee@stanford.edu.com"))          
        self.assertFalse(swot.is_academic("lee@strath.ac.uk.com"))          
        self.assertTrue(swot.is_academic("stanford.edu"))                  
        self.assertTrue(swot.is_academic("slac.stanford.edu"))             
        self.assertTrue(swot.is_academic("www.stanford.edu"))              
        self.assertTrue(swot.is_academic("http://www.stanford.edu"))       
        self.assertTrue(swot.is_academic("http://www.stanford.edu:9393"))  
        self.assertTrue(swot.is_academic("strath.ac.uk"))                  
        self.assertTrue(swot.is_academic("soft-eng.strath.ac.uk"))         
        self.assertTrue(swot.is_academic("ugr.es"))                        
        self.assertTrue(swot.is_academic("uottawa.ca"))                    
        self.assertTrue(swot.is_academic("mother.edu.ru"))                 
        self.assertTrue(swot.is_academic("ucy.ac.cy"))                     
        self.assertFalse(swot.is_academic("leerilly.net"))                  
        self.assertFalse(swot.is_academic("gmail.com"))                     
        self.assertFalse(swot.is_academic("stanford.edu.com"))              
        self.assertFalse(swot.is_academic("strath.ac.uk.com"))              
        self.assertFalse(swot.is_academic(""))
        self.assertFalse(swot.is_academic("the"))                           
        self.assertTrue(swot.is_academic(" stanford.edu"))                 
        self.assertTrue(swot.is_academic("lee@strath.ac.uk "))             
        self.assertFalse(swot.is_academic(" gmail.com "))                   
        self.assertTrue(swot.is_academic("lee@stud.uni-corvinus.hu"))      
        self.assertTrue(swot.is_academic("lee@harvard.edu"))               
        self.assertTrue(swot.is_academic("lee@mail.harvard.edu"))

        self.assertFalse(swot.is_academic("imposter@si.edu"))

    def test_school_names(self):
        self.assertTrue("University of Strathclyde" in swot.get_school_names("lreilly@cs.strath.ac.uk"))
        self.assertFalse("uka tarsadia university,bardoli" in swot.get_school_names("lreilly@cs.strath.ac.uk"))
        self.assertEqual("BRG Fadingerstraße Linz, Austria", swot.get_school_names("lreilly@fadi.at")[0])
        self.assertEqual("St. Petersburg State University", swot.get_school_names("max@spbu.ru ")[0])
        self.assertEqual(0, len(swot.get_school_names("foo@shop.com")))

if __name__ == "__main__":
    unittest.main()