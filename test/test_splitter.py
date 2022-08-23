import unittest

from src.splitter import split
from src.function_holder import FunctionHolder


class TestSplitter(unittest.TestCase):
    def test_linear(self):
        cases = [
            FunctionHolder(0, 1, '1', '-x + 4'),  # constant negative
            FunctionHolder(0, 2, '1', 'x + 4'),  # constant positive
            FunctionHolder(0, 3, '-x + 4', '1'),  # negative constant
            FunctionHolder(0, 4, 'x + 4', '1'),  # positive constant
            FunctionHolder(0, 5, '1', '1'),  # constant constant
            FunctionHolder(0, 6, '-x', '-x + 4'),  # negative negative
            FunctionHolder(0, 7, '-x + 4', 'x + 8'),  # negative positive
            FunctionHolder(0, 8, 'x', 'x + 6'),  # positive positive
            FunctionHolder(0, 9, 'x + 8', '-x + 4'),  # positive negative
        ]

        expected = [
            FunctionHolder(0, 1, 'foo', 'foo', False, False),  # constant negative
            FunctionHolder(0, 2, 'foo', 'foo', False, True),  # constant positive
            FunctionHolder(0, 3, 'foo', 'foo', False, False),  # negative constant
            FunctionHolder(0, 4, 'foo', 'foo', True, False),  # positive constant
            FunctionHolder(0, 5, 'foo', 'foo', False, False),  # constant constant
            FunctionHolder(0, 6, 'foo', 'foo', False, False),  # negative negative
            FunctionHolder(0, 7, 'foo', 'foo', False, True),  # negative positive
            FunctionHolder(0, 8, 'foo', 'foo', True, True),  # positive positive
            FunctionHolder(0, 9, 'foo', 'foo', True, False),  # positive negative
        ]

        for k in range(len(cases)):
            self.assertEqual(split(cases[k])[0].x_1, expected[k].x_1)
            self.assertEqual(split(cases[k])[0].x_2, expected[k].x_2)
            self.assertEqual(split(cases[k])[0].g1_is_increasing, expected[k].g1_is_increasing)
            self.assertEqual(split(cases[k])[0].g2_is_increasing, expected[k].g2_is_increasing)

    def test_polynomials(self):
        cases = [
            FunctionHolder(-1, 1, '1', 'x ** 2'),  # constant quadratic
            FunctionHolder(-1, 1, 'x ** 2', '(x - 0.5) ** 2 + 1'),  # quadratic quadratic
        ]

        expected = [
            [FunctionHolder(-1, 0, 'foo', 'foo', False, False), FunctionHolder(0, 1, 'foo', 'foo', False, True)],
            # constant quadratic
            [FunctionHolder(-1, 0, 'foo', 'foo', False, False), FunctionHolder(0, 0.5, 'foo', 'foo', True, False),
             FunctionHolder(0.5, 1, 'foo', 'foo', True, True)],  # quadratic quadratic
        ]

        for k in range(len(cases)):
            for i in range(len(expected[k])):
                self.assertEqual(split(cases[k])[i].x_1, expected[k][i].x_1)
                self.assertEqual(split(cases[k])[i].x_2, expected[k][i].x_2)
                self.assertEqual(split(cases[k])[i].g1_is_increasing, expected[k][i].g1_is_increasing)
                self.assertEqual(split(cases[k])[i].g2_is_increasing, expected[k][i].g2_is_increasing)


if __name__ == '__main__':
    unittest.main()
