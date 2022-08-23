from src.function_holder import FunctionHolder, parse
from math import *
from src.inverter import invert
import src.splitter as splitter
from src.combiner import combine

from sympy.parsing.latex import parse_latex


def run(input):
    """
    driver that splits the function int monotonc sections, inverts the 
    bounds of each and stitches them together
    """

    function = FunctionHolder(float(input[0]), float(input[1]), 
    input[2], input[3])
    split = splitter.split(function)
    out = []

    for inv in split:
        f = invert(inv)
        for func in f:
            if func.x_1 == func.x_2: continue
            if func.x_1 > func.x_2: 
                raise Exception('Invalid bounds.')

            out.append(func)

    combined = combine(function, out)
    for fh in combined:

        fh.x_1 = check_numeric(fh.x_1)
        fh.x_2 = check_numeric(fh.x_2)
        fh.g_1 = check_numeric(fh.g_1)
        fh.g_2 = check_numeric(fh.g_2)

    return combined

def check_numeric(num):
    
    try:
        if not float(num).is_integer(): return num
        return trunc(float(num))
    except:
        return num

