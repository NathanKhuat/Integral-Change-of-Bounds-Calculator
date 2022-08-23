import unittest

import src.algorithm as algorithm
from src.function_holder import FunctionHolder


class TestAlgorithm(unittest.TestCase):
    def test_linear(self):
        cases = [[0, 2, '1', '-x + 4'],  # case 1 0 0
                 [0, 3, '2x + 1', 'x + 4'],  # case 4 of 1 1
                 [0, 4, '2', 'x + 4'],  # case 2 of 0 1
                 [0, 2, 'x', '3']]  # case 2 of 1 0

        expected = [[FunctionHolder(1, 2, 0, 2), FunctionHolder(2, 4, 0, '4 - y')],  # case 1 0 0
                    [FunctionHolder(1, 4, 0, 'y/2 - 1/2'), FunctionHolder(4, 7, 'y - 4', 'y/2 - 1/2')],  # case 4 of 1 1
                    [FunctionHolder(2, 4, 0, 4), FunctionHolder(4, 8, 'y - 4', 4)],  # case 2 of 0 1
                    [FunctionHolder(0, 2, 0, 'y'), FunctionHolder(2, 3, 0, 2)]]  # case 2 of 1 0

        self.runTests(cases, expected)

    def test_polynomial(self):
        cases = [[0, 1, 'x**2', '1'], # quadratic
                [-1, 1, 'x**2', '1'], #quadratic
                [-1, 1, 'x**2', 'x + 2'], #quadratic
                [-1, 1, 'x**2', 'x + 3'], #quadratic
                [-1, 1,'3x**2 - 2x + 1', '-x + 7'], #tougher quadratic
                [-1, 1,'2x**2 - 7x + 1','-x + 9'], #tougher quadratic
                [-1, 3,'2x**2 - 7x + 1','-x + 9'], #tougher quadratic
                [0, 4,'2x**2 - 7x + 1','-x + 9'], #tougher quadratic
                [-1, 1,'(x - 1)*(x + 1)*x**2', 'x + 3'], #4 poly
                [-1, 1,'(x - 3)*(x + 3)*x**2', 'x + 3'], #tougher 4 poly
                [-1, 3,'(x - 3)*(x + 3)*x**2', 'x + 3'], #tough 4 poly
                [-3, 1,'(x - 3)*(x + 3)*x**2', 'x + 3'] #tough 4 poly
                 ]

        expected = [[FunctionHolder(0, 1, '0', 'sqrt(y)')],
                    [FunctionHolder(0, 1, '-sqrt(y)', 'sqrt(y)')],
                    [FunctionHolder(0, 1, '-sqrt(y)', 'sqrt(y)'), FunctionHolder(1, 3, 'y - 2', '1')],
                    [FunctionHolder(0, 1, '-sqrt(y)', 'sqrt(y)'), FunctionHolder(1, 2, '-1', '1'),
                    FunctionHolder(2, 4, 'y - 3', '1')],
                    [FunctionHolder(0.6666666666666666, 2, '1/3 - sqrt(3*y - 2)/3', 'sqrt(3*y - 2)/3 + 1/3', True, True), FunctionHolder(2, 6, '1/3 - sqrt(3*y - 2)/3', '1', True, True), FunctionHolder(6, 8, '-1', '7 - y', True, True)],
                    [FunctionHolder(-4, 8, '7/4 - sqrt(8*y + 41)/4', '1', True, True), FunctionHolder(8, 10, '7/4 - sqrt(8*y + 41)/4', '9 - y', True, True)],
                    [FunctionHolder(-5.125, -2, '7/4 - sqrt(8*y + 41)/4', 'sqrt(8*y + 41)/4 + 7/4', True, True), FunctionHolder(-2, 6, '7/4 - sqrt(8*y + 41)/4', '3', True, True), FunctionHolder(6, 10, '7/4 - sqrt(8*y + 41)/4', '9 - y', True, True)],
                    [FunctionHolder(-5.125, 1, '7/4 - sqrt(8*y + 41)/4', 'sqrt(8*y + 41)/4 + 7/4', True, True), FunctionHolder(1, 5, '0', 'sqrt(8*y + 41)/4 + 7/4', True, True), FunctionHolder(5, 9, '0', '9 - y', True, True)],
                    [FunctionHolder(-0.25, 0, '-sqrt(sqrt(4*y + 1)/2 + 1/2)', '-sqrt(1/2 - sqrt(4*y + 1)/2)', True, True), FunctionHolder(-0.25, 0, 'sqrt(1/2 - sqrt(4*y + 1)/2)', 'sqrt(sqrt(4*y + 1)/2 + 1/2)', True, True), FunctionHolder(0, 2, '-1', '1', True, True), FunctionHolder(2, 4, 'y - 3', '1', True, True)], 
                    [FunctionHolder(-8, 0, '-1', '-sqrt(9/2 - sqrt(4*y + 81)/2)', True, True), FunctionHolder(-8, 0, 'sqrt(9/2 - sqrt(4*y + 81)/2)', '1', True, True), FunctionHolder(0, 2, '-1', '1', True, True), FunctionHolder(2, 4, 'y - 3', '1', True, True)], 
                    [FunctionHolder(-20.25, 0, 'sqrt(9/2 - sqrt(4*y + 81)/2)', 'sqrt(sqrt(4*y + 81)/2 + 9/2)', True, True), FunctionHolder(-8, 0, '-1', '-sqrt(9/2 - sqrt(4*y + 81)/2)', True, True), FunctionHolder(0, 2, '-1', '3', True, True), FunctionHolder(2, 6, 'y - 3', '3', True, True)],
                    [FunctionHolder(-20.25, 0, '-sqrt(sqrt(4*y + 81)/2 + 9/2)', '-sqrt(9/2 - sqrt(4*y + 81)/2)', True, True), FunctionHolder(-8, 0, 'sqrt(9/2 - sqrt(4*y + 81)/2)', '1', True, True), FunctionHolder(0, 4, 'y - 3', '1', True, True)]
                    ]

        self.runTests(cases, expected)

    def test_double_polynomial(self):
        pass
    #FunctionHolder(-1, 1, 'x**2', '-(x)**2 + 6')
    #FunctionHolder(-1, 2, 'x**2', '-(x - 1)**2 + 6')

    def test_sqrt(self):
        cases = [[0, 1, '0', 'sqrt(x)'], #simple case
                [3, 9, '0', 'sqrt(x)'], #simple case
                [0, 5, '0.25x + 1', 'sqrt(x + 3)'], #harder case
                [-2, 1, 'x**2', 'sqrt(x + 25)'] #sqrt plus linear case
                ]

        expected = [[FunctionHolder(0, 1, 'y**2', '1', True, True)],
                    [FunctionHolder(0, 1.7320508075688772, '3', '9', True, True), FunctionHolder(1.7320508075688772, 3, 'y**2', '9', True, True)],
                    [FunctionHolder(1, 1.7320508075688772, '0', '4.0*y - 4.0', True, True), FunctionHolder(1.7320508075688772, 2.25, 'y**2 - 3', '4.0*y - 4.0', True, True), FunctionHolder(2.25, 2.8284271247461903, 'y**2 - 3', '5', True, True)],
                    [FunctionHolder(0, 1, '-sqrt(y)', 'sqrt(y)', True, True), FunctionHolder(1, 4, '-sqrt(y)', '1', True, True), FunctionHolder(4, 4.795831523312719, '-2', '1', True, True), FunctionHolder(4.795831523312719, 5.0990195135927845, 'y**2 - 25', '1', True, True)]
                    ]

        self.runTests(cases, expected)

    def test_log(self):
        cases = [
                [1, 2, '0', 'log(x, 2)'],#simple case
                [3, 5, '1', 'log(x, 2)'], #harder case
                ]

        expected = [
                    [FunctionHolder(0, 1, 'exp(y*log(2))', '2', True, True)],
                    [FunctionHolder(1, 1.5849625007211563, '3', '5', True, True), FunctionHolder(1.5849625007211563, 2.321928094887362, 'exp(y*log(2))', '5', True, True)]
                    ]

        self.runTests(cases, expected)

        def test_exponential(self):
            cases = [
                    [0, 1, '0', '2**x'],
                    [1, 4, 'x', '3**(x / 2)'],
                    [1, 4, 'x**2 * (1 / 2)', '3**(x / 2)']
                    ]

            expected = [
                        [FunctionHolder(0, 1, '0', '1', True, True), FunctionHolder(1, 2, 'log(y)/log(2)', '1', True, True)],
                        [FunctionHolder(1, 1.7320508075688772, '1', 'y', True, True), FunctionHolder(1.7320508075688772, 4, '2*log(y)/log(3)', 'y', True, True), FunctionHolder(4, 9, '2*log(y)/log(3)', '4', True, True)],
                        [FunctionHolder(0.5, 1.7320508075688772, '1', 'sqrt(2)*sqrt(y)', True, True), FunctionHolder(1.7320508075688772, 8, '2*log(y)/log(3)', 'sqrt(2)*sqrt(y)', True, True), FunctionHolder(8, 9, '2*log(y)/log(3)', '4', True, True)]
                        ]

            self.runTests(cases, expected)

    def runTests(self, cases, expected):
        for i in range(0, len(cases)):
            to_test = algorithm.run(cases[i])
            for k in range(0, len(to_test)):
                self.assertEqual(to_test[k].to_list(), expected[i][k].to_list(), msg='test #: ' + str(i + 1))


if __name__ == '__main__':
    unittest.main()
