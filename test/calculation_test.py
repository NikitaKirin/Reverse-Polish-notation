import unittest
import core.polishCalculation as calc


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
        self.assertEqual(result, 25)

    def test_calculate_with_functions(self):
        result = calc.calculate_polish('4 sqrt')
        self.assertEqual(result, 2)

    def test_calculate_with_functions_second(self):
        result = calc.calculate_polish('5 10 - abs')
        self.assertEqual(result, 5)

    def test_calculate_with_expression_inner_functions(self):
        result = calc.calculate_polish('3 3 * sqrt')
        self.assertEqual(result, 3)

    def test_calculate_with_trigonometry_functions(self):
        result = calc.calculate_polish('90 sin')
        self.assertEqual(result, 0.8939966636005579)

    def test_calculate_with_trigonometry_and_other_functions(self):
        result = calc.calculate_polish('8100 sqrt sin')
        self.assertEqual(result, 0.8939966636005579)


if __name__ == '__main__':
    unittest.main()
