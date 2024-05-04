# This is my custom functions file to make it easy to define and use functions for optimization algorithms fpr 2-parameter functions

import numpy as np
import sympy as sp

# Classical partial derivative definitions within functions
class f_eg4:
    @staticmethod
    def f(x, y) -> float:
        r = 3**(-x**2 - y**2)
        return 1/ (r + 1)

    @staticmethod
    def pdx(x, y, h=1e-7):
        return (f_eg4.f(x + h, y) - f_eg4.f(x, y)) / h

    @staticmethod
    def pdy(x, y, h=1e-7):
        return (f_eg4.f(x, y + h) - f_eg4.f(x, y)) / h

