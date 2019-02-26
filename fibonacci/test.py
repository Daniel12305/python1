import unittest
from fibonacci import fib



class FunktionTest(unittest.TestCase):
    
    def test5(self):
        self.assertEqual(fib(5), 5)
        print("10110101")
        
if __name__ == "__main__":
    unittest.main()