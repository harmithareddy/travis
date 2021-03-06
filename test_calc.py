import unittest
import calc

import requests

class Test_000_Calculator(unittest.TestCase):

    def test_single_digit(self):
        i = 0
        for c in '0123456789':
            self.assertEqual(calc.evaluate(c),i)
            i = i + 1
    
    def test_multiple_digits(self):
        self.assertEqual(calc.evaluate('99999'),99999)
        self.assertEqual(calc.evaluate('12345'),12345)
        self.assertEqual(calc.evaluate('99999'),99999)
        self.assertEqual(calc.evaluate('99'),99)
        self.assertEqual(calc.evaluate('00'),00)

    def test_negative_numbers(self):
        self.assertEqual(calc.evaluate('-123'),-123)
        self.assertEqual(calc.evaluate('-1'),-1)
        self.assertEqual(calc.evaluate('0'),0)
        self.assertEqual(calc.evaluate('---123'),-123)
        self.assertEqual(calc.evaluate('-----123'),-123)

    def test_floating_numbers(self):
        self.assertEqual(calc.evaluate('123.456'),123.456)
        self.assertEqual(calc.evaluate('-123.456'),-123.456)
        self.assertEqual(calc.evaluate('0123.456'),123.456)

    def test_hexadecimal_numbers(self):
        self.assertEqual(calc.evaluate('0x00'),0)
        self.assertEqual(calc.evaluate('0x10'),16)
        self.assertEqual(calc.evaluate('0xff'),255)
        self.assertEqual(calc.evaluate('0xFF'),255)

    def test_add_two_numbers(self):
        self.assertEqual(calc.evaluate('1+1'),2)
    

if __name__ == "__main__":
    unittest.main(verbosity=2)
