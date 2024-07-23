import numpy as np
from ej1 import intenumcomp

print("                     LAB 5 - EJERCICIO 2\n")

f = lambda x : np.e**(-x)

metodos = ["trapecio","pm","simpson"]
subintervalos = [4,10,20]

for x in metodos:
    print(f"Error absoluto con regla compuesta del {x}\n")
    for y in subintervalos:
        print(f"    Con {y} subintervalos: {abs(intenumcomp(f,0,1,y,x)-(1-1/np.e))}\n")