import numpy as np
from ej1 import intenumcomp
from graphic_function import graphic

def senit(x):
    return [intenumcomp(np.cos,0,xi,10*xi,"trapecio") for xi in x]

x = np.arange(0,2*np.pi,0.5)

graphic([x]*2,[[np.sin(xi) for xi in x],senit(x)],["sen(x)","senit(x)"],"Aproximación con integración numérica",True,1,[True]*2)
