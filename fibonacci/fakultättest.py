from fakultät import fakultät
import unittest

class FunktionTest(unittest.TestCase):
    
    def test5(self):
        self.assertEqual(fakultät(5), 120)

        
if __name__ == "__main__":
    unittest.main()