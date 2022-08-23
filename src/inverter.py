from math import *
from sympy import *
from src.function_holder import FunctionHolder, parse


def invert(function):

    out = []
    g1_parsed = str(parse(function.g_1))
    g2_parsed = str(parse(function.g_2))

    x = function.x_2
    lower_right = change_int(eval(g1_parsed))
    upper_right = change_int(eval(g2_parsed))
    x = function.x_1
    upper_left = change_int(eval(g2_parsed))
    lower_left = change_int(eval(g1_parsed))


    def find_inverted_in_bounds(inverted, input):
        epsil = 0.0000001
        midpoint = function.x_2 + (function.x_1 - function.x_2) / 2
        x = midpoint
        y__at_midpoint = eval(str(parse(input)))

        for func in inverted:
            
            y = y__at_midpoint
            eval_midpoint = eval(str(func))
            
            if eval_midpoint - epsil < float(midpoint) < eval_midpoint + epsil:
                return func
            

    def invert_funcs() -> list:
        x, y = symbols('x'), symbols('y')

        invert_g_1 = solve(parse(function.g_1) - y, x), function.g_1
        invert_g_2 = solve(parse(function.g_2) - y, x), function.g_2

        inverted = [
            find_inverted_in_bounds(invert_g_1), 
            find_inverted_in_bounds(invert_g_2)
            ]
        
        return inverted

    inverted_funcs = invert_funcs()


    def invert_upper_c(inv=False) -> FunctionHolder:
        """invert_upper_c addresses the case where the upper bound of the 
        integral is a constant.

        :return: FuncHolder of invert-upper-constant integral
        """
        if inv:

            if lower_left < upper_right:
                return FunctionHolder(lower_right, lower_left, 
                inverted_funcs[0], function.x_2)

            return FunctionHolder(lower_right, upper_right, inverted_funcs[0], 
            function.x_2)

        if upper_left < lower_right:
            return FunctionHolder(lower_left, upper_left, function.x_1, 
            inverted_funcs[0])

        return FunctionHolder(lower_left, lower_right, function.x_1, 
        inverted_funcs[0])

    def invert_lower_c(inv=False) -> FunctionHolder:
        """invert_lower_c addresses the case where the lower bound of the 
        integral is a constant.

        :return: FuncHolder of invert-lower-constant integral
        """
        if inv:

            if upper_right > lower_left:
                return FunctionHolder(upper_right, upper_left, function.x_1, 
                inverted_funcs[1])

            return FunctionHolder(lower_left, upper_left, function.x_1, 
            inverted_funcs[1])

        if upper_left < lower_right:
            return FunctionHolder(lower_right, upper_right, inverted_funcs[1], 
            function.x_2)

        return FunctionHolder(upper_left, upper_right, inverted_funcs[1], 
        function.x_2)

    def invert_all_f(inv=False) -> FunctionHolder:
        """invert_all_f addresses the case where both the upper and lower 
        bounds of the integrals are functions that
        need to be inverted by wra.

        :return: FuncHolder of invert-all-functions integral
        """
        if inv:
            return FunctionHolder(upper_right, lower_left, inverted_funcs[0], 
            inverted_funcs[1])

        return FunctionHolder(upper_left, lower_right, inverted_funcs[1], 
        inverted_funcs[0])

    def invert_all_c(lower_b, upper_b) -> FunctionHolder:
        """invert_all_c addresses the case where both the upper and lower 
        bounds of the integral are constants.
        They are simply swapped.

        :param upper_b:
        :param lower_b:
        :param function: ur input function
        :return: uncHolder of invert-all-constants integral
        """
        return FunctionHolder(lower_b, upper_b, function.x_1, function.x_2)

    # 0 0
    if not function.g1_is_increasing and not function.g2_is_increasing:

        if lower_left == lower_right:

            if lower_right != upper_right:
                # case 1 of 0 0
                out.append(invert_all_c(lower_right, upper_right))  
            # case 2 of 0 0
            out.append(invert_lower_c(inv=True))  

        elif upper_right == upper_left:
            
            if lower_left != upper_left:
                # case 6 of 0 0
                out.append(invert_all_c(lower_left, upper_left))  
            # case 7 of 0 0
            out.append(invert_upper_c(inv=True))  

        else:

            if lower_right == upper_right:
                # case 8 of 0 0
                out.append(invert_all_f(inv=True))
                out.append(invert_lower_c(inv=True))  

            elif lower_left == upper_left:
                # case 9 of 0 0
                out.append(invert_all_f(inv=True))
                out.append(invert_upper_c(inv=True))  

            else:

                if upper_right < lower_left:
                    # case 5 of 0 0
                    out.append(invert_all_f(inv=True))  

                elif upper_right > lower_left:
                    # case 4 of 0 0
                    out.append(invert_all_c(lower_left, upper_right))  
                # case 3 of 0 0
                out.append(invert_upper_c(inv=True))  
                out.append(invert_lower_c(inv=True))

    # 0 1
    elif not function.g1_is_increasing:  

        if lower_left == lower_right:

            if lower_left != upper_left:
                # case 2 of 0 1
                out.append(invert_all_c(lower_left, upper_left))  
            # case 1 of 0 1
            out.append(invert_lower_c())  

        else:

            if lower_left != upper_left:
                # case 4 of 0 1
                out.append(invert_all_c(lower_left, upper_left))  
            # case 3 of 0 1
            out.append(invert_lower_c())  
            out.append(invert_upper_c(inv=True))
    
    # 1 0
    elif not function.g2_is_increasing: 

        if upper_left == upper_right:

            if upper_right != lower_right:
                # case 6 of 1 0
                out.append(invert_all_c(lower_right, upper_right))  
            # case 5 of 1 0
            out.append(invert_upper_c())  

        else:

            if upper_right != lower_right:
                # case 8 of 1 0
                out.append(invert_all_c(lower_right, upper_right))  
            # case 7 of 1 0
            out.append(invert_upper_c())  
            out.append(invert_lower_c(inv=True))
    
    # 1 1
    else: 

        if lower_left == upper_left:
            # case 5 of 1 1
            out.append(invert_lower_c())  
            out.append(invert_all_f())

        elif lower_right == upper_right:
            # case 4 of 1 1
            out.append(invert_upper_c())  
            out.append(invert_all_f())
        
        else:

            if lower_right < upper_left:
                # case 2 of 1 1
                out.append(invert_all_c(lower_right, upper_left))  

            if upper_left < lower_right:
                # case 3 of 1 1
                out.append(invert_all_f())  
            # case 1 of 1 1
            out.append(invert_upper_c())  
            out.append(invert_lower_c())


    out.sort(key= (lambda x: x.x_1))
    return out

def change_int(num):
    if not float(num).is_integer(): return float(num)
    return int(num)
