import unittest
from src.function_holder import parse, FunctionHolder
from sympy import *


class TestFunctionHolder(unittest.TestCase):

    def test_parse(self):
        self.assertEqual(str(parse('2x')), '2*x')
        # self.assertEqual(str(parse('2^x')), '2**x')
        self.assertEqual(str(parse('x y 3')), 'x*y*3')

    def test_evaluate(self):
        function = FunctionHolder(1, 3, 'x', '2x')
        self.assertEqual(eval(str(parse(function.g_1)), {'x': function.x_1}), 1)
        self.assertEqual(eval(str(parse(function.g_1)), {'x': function.x_2}), 3)
        self.assertEqual(eval(str(parse(function.g_2)), {'x': function.x_1}), 2)
        self.assertEqual(eval(str(parse(function.g_2)), {'x': function.x_2}), 6)

        function = FunctionHolder(-3, -1, '2x', 'x')
        self.assertEqual(eval(str(parse(function.g_1)), {'x': function.x_1}), -6)
        self.assertEqual(eval(str(parse(function.g_1)), {'x': function.x_2}), -2)
        self.assertEqual(eval(str(parse(function.g_2)), {'x': function.x_1}), -3)
        self.assertEqual(eval(str(parse(function.g_2)), {'x': function.x_2}), -1)


if __name__ == '__main__':
    unittest.main()
