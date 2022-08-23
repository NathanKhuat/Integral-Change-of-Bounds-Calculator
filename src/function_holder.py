from sympy import *
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication

def parse(func) -> exp:
    """
    Takes a string and formats it. i.e. 2x -> 2*x
    :param func: string representation of a function
    :return: string representation of a function with correct formatting
    """
    transformations = standard_transformations + (implicit_multiplication,)
    return parse_expr(func, transformations=transformations, evaluate=False)


class FunctionHolder:
    def __init__(self, lower, upper, lower_func, upper_func, 
    g1_is_increasing=True, g2_is_increasing=True):
        """Initializes bounds and functions.

        x - symbol used for solving"""
        self.x_1 = lower
        self.x_2 = upper
        self.g_2 = upper_func
        self.g_1 = lower_func
        self.g1_is_increasing = g1_is_increasing
        self.g2_is_increasing = g2_is_increasing

    def __repr__(self) -> str:
        return f"{self.x_1}, {self.x_2}, {self.g_1}, {self.g_2}, {self.g1_is_increasing}, {self.g2_is_increasing}"

    def to_list(self):
        return [str(self.x_1), str(self.x_2), str(self.g_1), str(self.g_2),
        str(self.g1_is_increasing), str(self.g2_is_increasing)]
