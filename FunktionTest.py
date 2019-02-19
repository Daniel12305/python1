import unittest
from Funktion import romanNumber

class FunktionTest(unittest.TestCase):
    
    def testVI(self):
        self.assertEqual(romanNumber(6), "VI")
        
    def testV(self):
        self.assertEqual(romanNumber(5), "V")
        
    def testVII(self):
        self.assertEqual(romanNumber(7), "VII")
        print("VII")

    def testIII(self):
        self.assertEqual(romanNumber(3), "III")
        print("III")
        
    def testXXVII(self):
        self.assertEqual(romanNumber(27), "XXVII")
    
    def testXX(self):
        self.assertEqual(romanNumber(20), "XX")
        
    def testIX(self):
        self.assertEqual(romanNumber(9), "IX")
        
    def testIV(self):
        self.assertEqual(romanNumber(4), "IV")
        
    def testXL(self):
        self.assertEqual(romanNumber(40), "XL")
        
    def testL(self):
        self.assertEqual(romanNumber(50), "L")
        
    def testXLIX(self):
        self.assertEqual(romanNumber(49), "XLIX")

    def testLIX(self):
        self.assertEqual(romanNumber(59), "LIX")
        
    def testMMMCMXCIX(self):
        self.assertEqual(romanNumber(3999), "MMMCMXCIX")

    def testMMXIX(self):
        self.assertEqual(romanNumber(2019), "MMXIX")

    def testMCMLXXXIV(self):
        self.assertEqual(romanNumber(1984), "MCMLXXXIV")
    

if __name__ == "__main__":
    unittest.main()