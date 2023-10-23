import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        result = self.calc.add(2, 2)
        self.assertEqual(result, 4)

    def test_subtraction(self):
        result = self.calc.subtract(4, 2)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
