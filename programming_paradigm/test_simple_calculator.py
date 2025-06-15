import unittest
from simple_calculator import SimpleCalculator

class TestClass(unittest.TestCase):

    def testClass(self):
        self.calc = SimpleCalculator()
        

    def test_addition(self):
        self.assertEqual(self.calc.add(5,4),9)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8,10),-2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(15,3),5)

    def test_Division(self):
        self.assertEqual(self.calc.divide(9,3),3)
        with self.assertRaises(ValueError):
            self.calc.divide(10,0)
            
