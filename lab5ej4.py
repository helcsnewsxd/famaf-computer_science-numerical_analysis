import numpy as np
from lab5ej1 import intenumcomp

f = lambda x : x * np.e**(-x)
g = lambda x : x * np.sin(x)
h = lambda x : (1+x**2)**(3/2)

func = [f,g,h]
met = ["trapecio","simpson"]
n = [130]

print("                 LAB 5 - EJERCICIO 4\n")
print(f"Inciso A con 130 puntos: {  } \n")
