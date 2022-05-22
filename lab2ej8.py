from ej3 import rnewton
import numpy as np
from sympy import *

def min_function():
    def function(a): #1st and 2nd derivate to calculate the position of the minimum value into (0,pi/2) using the newton method
        #we're using a not numeric method to calculate the derivatives to except the finit error and not calculate this manually

        x = Symbol('x')
        f = tan(x)/x**2
        df = f.diff(x)
        ddf = df.diff(x)

        f = lambdify(x,f)
        df = lambdify(x,df)
        ddf = lambdify(x,ddf)

        return df(a),ddf(a)
    
    px,py = rnewton(function, 1, 1e-10, 10**7)

    return px[-1]
