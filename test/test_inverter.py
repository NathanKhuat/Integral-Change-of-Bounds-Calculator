import unittest

from src.inverter import Inverter
from src.function_holder import FunctionHolder


class TestInverter(unittest.TestCase):
    def test_case_0_0(self):
        cases = [
            FunctionHolder(0, 2, '1', '-x + 4', False, False),  # case 1 0 0
            FunctionHolder(0, 3, '1', '-x + 4', False, False),  # case 2 0 0
            FunctionHolder(0, 5, '-(1/2)x + 1', '-x + 6', False, False),  # case 3 of 0 0
            FunctionHolder(0, 5, '-(1/2)x + 1', '-x + 8', False, False),  # case 4 of 0 0
            FunctionHolder(0, 3, '-(1/2)x + 2', '-x + 4', False, False),  # case 5 of 0 0
            FunctionHolder(0, 3, '-x + 3', '4', False, False),  # case 6 of 0 0
            FunctionHolder(0, 3, '-x + 3', '3', False, False),  # case 7 of 0 0
            FunctionHolder(0, 4, '-(1/2)x + 3', '-x + 5', False, False),  # case 8 of 0 0
            FunctionHolder(0, 4, '-x + 5', '-(1/2)x + 5', False, False),  # case 9 of 0 0
        ]

        expected = [
            [FunctionHolder(1, 2, 0, 2), FunctionHolder(2, 4, 0, '4 - y')],  # case 1 0 0
            [FunctionHolder(1, 4, 0, '4 - y')],  # case 2 0 0
            [FunctionHolder(-1.5, 1, '2 - 2*y', 5), FunctionHolder(1, 6, 0, '6 - y')],  # case 3 of 0 0
            [FunctionHolder(-1.5, 1, '2 - 2*y', 5), FunctionHolder(1, 3, 0, 5),
             FunctionHolder(3, 8, 0, '8 - y')],  # case 4 of 0 0
            [FunctionHolder(0.5, 1, '4 - 2*y', 3), FunctionHolder(1, 2, '4 - 2*y', '4 - y'),
             FunctionHolder(2, 4, 0, '4 - y')],  # case 5 of 0 0
            [FunctionHolder(0, 3, '3 - y', 3), FunctionHolder(3, 4, 0, 3)],  # case 6 of 0 0
            [FunctionHolder(0, 3, '3 - y', 3)],  # case 7 of 0 0
            [FunctionHolder(1, 3, '6 - 2*y', '5 - y'), FunctionHolder(3, 5, 0, '5 - y')],  # case 8 of 0 0
            [FunctionHolder(1, 3, '5 - y', 4), FunctionHolder(3, 5, '5 - y', '10 - 2*y')]  # case 9 of 0 0
        ]

        self.runTests(cases, expected)

    def test_case_1_1_1(self):
        cases = [
            FunctionHolder(0, 3, 'x', 'x + 3', True, True),  # case 1 of 1 1
        ]
        expected = [
            [FunctionHolder(0, 3, 0, 'y'), FunctionHolder(3, 6, 'y - 3', 3)],  # case 1 of 1 1
        ]

        self.runTests(cases, expected)

    def test_case_1_1(self):
        cases = [
            FunctionHolder(0, 3, 'x', 'x + 3', True, True),  # case 1 of 1 1
            FunctionHolder(0, 3, 'x', 'x + 4', True, True),  # case 2 of 1 1
            FunctionHolder(0, 3, '2x', 'x + 4', True, True),  # case 3 of 1 1
            FunctionHolder(0, 3, '2x + 1', 'x + 4', True, True),  # case 4 of 1 1
            FunctionHolder(0, 5, '(1/2)x + 2', 'x + 2', True, True),  # case 5 of 1 1
        ]

        expected = [
            [FunctionHolder(0, 3, 0, 'y'), FunctionHolder(3, 6, 'y - 3', 3)],  # case 1 of 1 1
            [FunctionHolder(0, 3, 0, 'y'), FunctionHolder(3, 4, 0, 3), FunctionHolder(4, 7, 'y - 4', 3)],
            # case 2 of 1 1
            [FunctionHolder(0, 4, 0, 'y/2'), FunctionHolder(4, 6, 'y - 4', 'y/2'), FunctionHolder(6, 7, 'y - 4', 3)],
            # case 3 of 1 1
            [FunctionHolder(1, 4, 0, 'y/2 - 1/2'), FunctionHolder(4, 7, 'y - 4', 'y/2 - 1/2')],  # case 4 of 1 1
            [FunctionHolder(2, 4.5, 'y - 2', '2*y - 4'), FunctionHolder(4.5, 7, 'y - 2', 5)],  # case 5 of 1 1
        ]

        self.runTests(cases, expected)

    def test_case_0_1(self):
        cases = [
            FunctionHolder(0, 4, '2', 'x + 2', False, True),  # case 1 of 0 1
            FunctionHolder(0, 4, '2', 'x + 4', False, True),  # case 2 of 0 1
            FunctionHolder(0, 4, '-x + 3', 'x + 3', False, True),  # case 4 of 0 1
            FunctionHolder(0, 4, '-x + 3', 'x + 4', False, True),  # case 5 of 0 1
        ]

        expected = [
            [FunctionHolder(2, 6, 'y - 2', 4)],  # case 1 of 0 1
            [FunctionHolder(2, 4, 0, 4), FunctionHolder(4, 8, 'y - 4', 4)],  # case 2 of 0 1
            [FunctionHolder(-1, 3, '3 - y', 4), FunctionHolder(3, 7, 'y - 3', 4)],  # case 4 of 0 1
            [FunctionHolder(-1, 3, '3 - y', 4), FunctionHolder(3, 4, 0, 4), FunctionHolder(4, 8, 'y - 4', 4)]
            # case 5 of 0 1
        ]

        self.runTests(cases, expected)

    def test_case_1_0(self):
        cases = [
            FunctionHolder(0, 3, 'x', '3', True, False),  # case 1 of 1 0
            FunctionHolder(0, 2, 'x', '3', True, False),  # case 2 of 1 0
            FunctionHolder(0, 2, 'x', '-x + 6', True, False),  # case 3 of 1 0
            FunctionHolder(0, 3, 'x', '-x + 6', True, False)  # case 4 of 1 0
        ]

        expected = [
            [FunctionHolder(0, 3, 0, 'y')],  # case 1 of 0 1
            [FunctionHolder(0, 2, 0, 'y'), FunctionHolder(2, 3, 0, 2)],  # case 2 of 1 0
            [FunctionHolder(0, 2, 0, 'y'), FunctionHolder(2, 4, 0, 2), FunctionHolder(4, 6, 0, '6 - y')],
            # case 3 of 1 0
            [FunctionHolder(0, 3, 0, 'y'), FunctionHolder(3, 6, 0, '6 - y')]  # case 4 of 1 0
        ]

        self.runTests(cases, expected)

    def runTests(self, cases, expected):
        for i in range(0, len(cases)):
            to_test = Inverter(cases[i]).invert()
            for k in range(0, len(to_test)):
                self.assertEqual(to_test[k].to_list(), expected[i][k].to_list(), msg='test #: ' + str(i + 1))


if __name__ == '__main__':
    unittest.main()
