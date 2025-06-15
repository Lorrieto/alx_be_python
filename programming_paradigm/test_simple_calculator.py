import unittest
from simple_calculator import SimpleCalculator

class TestClass(unittest.TestCase):

    def testClass(self):
        self.testClass = SimpleCalculator()
        

    def test_addition(self):
        self.assertEqual(self.testClass.add(5,4),9)

    def test_subtraction(self):
        self.assertEqual(self.testClass.subtract(8,10),-2)

    def test_multiplication(self):
        self.assertEqual(self.testClass.multiply(15,3),5)

    def test_Division(self):
        self.assertEqual(self.testClass.divide(9,3),3)
        with self.assertRaises(ValueError):
            self.testClass.divide(10,0)
            
