import unittest
import core.transformationToPolish as trasform


class MyTestCase(unittest.TestCase):
    def test_easy_expression(self):
        result = trasform.transform_to_polish('3 + 4')
        self.assertEqual(result, '3 4 +')

    def test_easy_arithmetic_expression(self):
        result = trasform.transform_to_polish('3 + 4 * 5')
        self.assertEqual(result, '3 4 5 * +')

    def test_expression_with_brackets(self):
        result = trasform.transform_to_polish('( 3 + 4 ) * 5')
        self.assertEqual(result, '3 4 + 5 *')

    def test_expression_with_pow(self):
        result = trasform.transform_to_polish('3 ^ 2 + 5 * 6')
        self.assertEqual(result, '3 2 ^ 5 6 * +')

    def test_expression_with_easy_functions(self):
        result = trasform.transform_to_polish('1 + cos ( 45 )')
        self.assertEqual(result, '1 45 cos +')

    def test_expression_with_easy_functions_second(self):
        result = trasform.transform_to_polish('abs ( 5 + 5 )')
        self.assertEqual(result, '5 5 + abs')

    def test_expression_with_normal_functions(self):
        result = trasform.transform_to_polish('1 + sin ( 40 + 5 ) * 10')
        self.assertEqual(result, '1 40 5 + sin 10 *')

    def test_expression_with_hard_functions(self):
        result = trasform.transform_to_polish('sin ( deg ( 90 ) )')
        self.assertEqual(result, '90 deg sin')

    def test_hard_expression(self):
        result = trasform.transform_to_polish('1 ^ 3 / ( 5 * 4 ) + 10 * sin ( 10 * 4 )')
        self.assertEqual(result, '1 3 ^ 5 4 * / 10 10 4 * sin * +')


if __name__ == '__main__':
    unittest.main()
