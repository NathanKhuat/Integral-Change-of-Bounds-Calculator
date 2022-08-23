from sympy import *
from src.function_holder import FunctionHolder, parse
import src.splitter as splitter
from math import *


#combines the partitioned integrals back together
def combine(function, func_list):

    roots = splitter.deriv_roots(function)
    roots.sort()

    for r in roots:
        if function.x_1 > r or function.x_2 < r: roots.remove(r)

    if not roots: return func_list

    x = function.x_1
    a = eval(str(parse(function.g_1)))
    c = eval(str(parse(function.g_2)))
    x = function.x_2
    b = eval(str(parse(function.g_1)))
    d = eval(str(parse(function.g_2)))

    bound_intersects = [a, b, c, d]
    bound_intersects.sort()

    combined = []

    # concavity
    upp_concav = diff(diff(str(parse(function.g_1)), 'x'), 'x')

    concave_up = True
    x = (function.x_2 - function.x_1) / 2 #midpoint
    if eval(str(upp_concav)) < 0: concave_up = False


    #extranous 
    extran_funcs = []
    i = min(bound_intersects[2], bound_intersects[3])
    j = max(bound_intersects[2], bound_intersects[3])
    if not concave_up:
        i = max(bound_intersects[1], bound_intersects[0])
        j = min(bound_intersects[1], bound_intersects[0])

    for f in func_list.copy():

        if not concave_up:
            if f.x_1 >= i: continue
            if f.x_2 <= i: extran_funcs.append(f) 
            else:
                func_list.append(FunctionHolder(i, f.x_2, f.g_1, f.g_2))
                extran_funcs.append(FunctionHolder(f.x_1, i, f.g_1, f.g_2))
            func_list.remove(f)
            continue

        if f.x_2 <= i: continue
        if f.x_1 >= i: extran_funcs.append(f)
        else:
            func_list.append(FunctionHolder(f.x_1, i, f.g_1, f.g_2))
            extran_funcs.append(FunctionHolder(i, f.x_2, f.g_1, f.g_2))
        func_list.remove(f)

    if extran_funcs:
        l_f, u_f = None, None
        for g_f in extran_funcs:

            if not concave_up:
                if g_f.x_1 == j:
                    l_f = g_f.g_1
                    u_f = g_f.g_2
                    combined.append(FunctionHolder(j, i, l_f, u_f))
                    continue

            if g_f.x_2 == j:
                u_f = g_f.g_2
                l_f = g_f.g_1
                combined.append(FunctionHolder(i, j, l_f, u_f))
    

    #sort
    to_combine_lower, to_combine_upper = {}, {}
    find_x_1 = (lambda x: x.x_1)
    find_x_2 = (lambda x: x.x_2)

    for root in roots:
        to_combine_lower[root], to_combine_upper[root] = [], []

        for func in func_list.copy():
           
            if str(func.g_2) == str(root): 
                if root == roots[0] or func.g_1 not in roots:
                        to_combine_upper[root].append(func)
                        func_list.remove(func)
            elif str(func.g_1) == str(root):
                    to_combine_lower[root].append(func)
                    func_list.remove(func)

        if not concave_up:
            to_combine_lower[root].sort(key= find_x_1, reverse=True)
            to_combine_upper[root].sort(key= find_x_1, reverse=True)
            continue

        to_combine_lower[root].sort(key= find_x_2)
        to_combine_upper[root].sort(key= find_x_2)

    combined += func_list


    #combiner 
    for i in range(len(roots)):
        lower, upper = to_combine_lower[roots[i]], to_combine_upper[roots[i]]

        temp = []

        while lower and upper:
            case_c_u = concave_up and lower[0].x_2 != upper[0].x_2
            case_c_d = not concave_up and lower[0].x_1 != upper[0].x_1
            if case_c_d or case_c_u:
                if case_c_u:
                    if lower[0].x_2 > upper[0].x_2 :
                        funcs = [upper[0], lower[0]] 
                    else: [lower[0], upper[0]]

                    temp = FunctionHolder(funcs[0].x_2, funcs[1].x_2, 
                    funcs[1].g_1, funcs[1].g_2)
                else:
                    if lower[0].x_1 > upper[0].x_1:
                        funcs = [lower[0], upper[0]]  
                    else: [upper[0], lower[0]]

                    temp = FunctionHolder(funcs[1].x_1, funcs[0].x_1, 
                    funcs[1].g_1, funcs[1].g_2)
                
                if funcs[1] in lower:
                        lower.remove(funcs[1])
                        lower.insert(0, temp)
                        lower.insert(0, FunctionHolder(funcs[0].x_1, 
                        funcs[0].x_2, funcs[1].g_1, funcs[1].g_2))
                else:
                    upper.remove(funcs[1])
                    upper.insert(0, temp)
                    upper.insert(0, FunctionHolder(funcs[0].x_1, 
                    funcs[0].x_2, funcs[1].g_1, funcs[1].g_2)) 

            merged = FunctionHolder(lower[0].x_1, upper[0].x_2, 
            upper[0].g_1, lower[0].g_2)

            if i + 1 < len(roots):
                if str(merged.g_2) == str(roots[i + 1]):
                    temp.append(merged)
                else: combined.append(merged)
            else:
                combined.append(merged)
            lower.pop(0)
            upper.pop(0)
        
        if i + 1 < len(roots):
            to_combine_upper[roots[i + 1]] += temp

    #last check
    combined.sort(key=find_x_1)

    c = combined.copy()
    for i in range(len(c) - 1):
        for j in range(1, len(c)):
            if c[i].x_2 != c[j].x_1: continue 

            if c[i].g_1 == c[j].g_1 and c[i].g_2 == c[j].g_2:
                combined.remove(c[i])
                combined.remove(c[j])
                combined.append(FunctionHolder(c[i].x_1, c[j].x_2, 
                c[i].g_1, c[j].g_2))

    combined.sort(key=find_x_1)

    return combined

