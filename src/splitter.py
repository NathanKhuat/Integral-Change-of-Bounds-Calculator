from sympy import *
from src.function_holder import FunctionHolder, parse


def split(function) -> list:

    # take the derivative of each function
    g1_derivative = diff(str(parse(function.g_1)), 'x')
    g2_derivative = diff(str(parse(function.g_2)), 'x')
   
    # compile a sorted list of where the derivative of each function is equal 
    # to zero
    # this will be where each function has the potential to change from 
    # increasing to decreasing
    derivative_roots = solve(g1_derivative) + solve(g2_derivative)
    derivative_roots.sort()

    # find the places to split i.e. the bounds and where derivative is zero 
    # inside the bounds
    in_bounds = [function.x_1]
    for value in derivative_roots:
        if function.x_1 < value < function.x_2:
            in_bounds.append(value)
    in_bounds.append(function.x_2)

    # creates a list of FunctionHolders which are split at the bound and have 
    # is_increasing updated for future logic
    to_return = []
    for i in range(len(in_bounds) - 1):

        midpoint = ((in_bounds[i] + in_bounds[i + 1]) / 2)

        x = midpoint
        g_1_is_increasing = eval(str(g1_derivative)) > 0
        g_2_is_increasing =  eval(str(g2_derivative)) > 0
        
        to_return.append(FunctionHolder(in_bounds[i], in_bounds[i + 1], 
        function.g_1, function.g_2, g_1_is_increasing, g_2_is_increasing))

    return to_return

def deriv_roots(function):
    g1_deriv = diff(str(parse(function.g_1)), 'x')
    g2_deriv = diff(str(parse(function.g_2)), 'x')

    derivative_roots = solve(g1_deriv) + solve(g2_deriv)
    return derivative_roots

