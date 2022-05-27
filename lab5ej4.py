import numpy as np
from lab5ej1 import intenumcomp

f = lambda x : x * np.e**(-x)
g = lambda x : x * np.sin(x)
h = lambda x : (1+x**2)**(3/2)

func = [f,g,h]
met = ["trapecio","simpson"]
n = [[130,200],[200,200],[200,200]]
ej = ["A","B","C"]

print("                 LAB 5 - EJERCICIO 4\n")

for i in range(0,3):
  print(f"Inciso {ej[i]}:")
  for j in range(0,2):
    x = intenumcomp(f[i],0,1,n[i][j])
    print(f"        {met[j]} con {n[i][j]} intervalos: {x}")
