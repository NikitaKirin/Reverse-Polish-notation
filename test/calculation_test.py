import unittest
import core.polishCalculation as calc
import math


class MyTestCase(unittest.TestCase):
    def test_calculate_easy_expression(self):
        result = calc.calculate_polish('3 4 +')
        self.assertEqual(result, 7)

    def test_calculate_with_arithmetic_operations_plus_minus(self):
        result = calc.calculate_polish('3 4 5 6 + + -')
        self.assertEqual(result, -12)

    def test_second_calculate_with_arithmetic_operations_mul_div(self):
        result = calc.calculate_polish('5 6 * 10 /')
        self.assertEqual(result, 3)

    def test_calculate_with_div(self):
        result = calc.calculate_polish('7 2 div')
        self.assertEqual(result, 3)

    def test_calculate_with_mod(self):
        result = calc.calculate_polish('7 2 %')
        self.assertEqual(result, 1)

    def test_calculate_with_plus_mul(self):
        result = calc.calculate_polish('3 4 5 * +')
        self.assertEqual(result, 23)

    def test_calculate_with_plus_minus_mul_div(self):
        result = calc.calculate_polish('1 4 5 * + 1 -')
        self.assertEqual(result, 20)

    def test_calculate_with_pow(self):
        result = calc.calculate_polish('5 2 ^')
        self.assertEqual(result, 5 ** 2)

    def test_calculate_with_functions(self):
        result = calc.calculate_polish('4 sqrt')
        self.assertEqual(result, 2)

    def test_calculate_with_functions_second(self):
        result = calc.calculate_polish('5 10 - abs')
        self.assertEqual(result, 5)

    def test_calculate_with_expression_inner_functions(self):
        result = calc.calculate_polish('3 3 * sqrt')
        self.assertEqual(result, math.sqrt(3 * 3))

    def test_calculate_with_trigonometry_functions(self):
        result = calc.calculate_polish('90 sin')
        self.assertEqual(result, math.sin(90))

    def test_calculate_with_hard_trigonometry_functions(self):
        result = calc.calculate_polish('0 deg cos')
        self.assertEqual(result, math.cos(math.radians(0)))

    def test_calculate_with_trigonometry_and_other_functions(self):
        result = calc.calculate_polish('8100 sqrt sin')
        self.assertEqual(result, math.sin(math.sqrt(8100)))

    def test_calculate_exp_function(self):
        result = calc.calculate_polish('2 exp')
        self.assertEqual(result, math.exp(2))

    def test_calculate_log_functions(self):
        result = calc.calculate_polish('100 10 log')
        self.assertEqual(result, math.log(100, 10))


if __name__ == '__main__':
    unittest.main()
