from sympy.printing import latex
from sympy import *
import re

class LatexConverter():
    
    def convert(expression):

        tex = latex(expression)

        logarithm = re.compile(r'\\frac\{(.*)\s*\\log\{\\left\(y \\right\)\}\}\{\\log\{\\left\((\d)* \\right\)\}\}')
        
        # \frac{2 \log{\left(y \right)}}{\log{\left(3 \right)}}

        test = logarithm.search(tex)

        while test:
            
            multiplier = test.group(1)
            log_base = '{' + test.group(2) + '}'
            if multiplier:
                tex = tex.replace(test.group(), f'{multiplier} \log_{log_base}y')
            else:
                tex = tex.replace(test.group(), f'\log_{log_base}y')

        return tex
