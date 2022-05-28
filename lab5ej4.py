import numpy as np
from lab5ej1 import intenumcomp

f = lambda x : x * np.e**(-x)
g = lambda x : x * np.sin(x)
h = lambda x : (1+x**2)**(3/2)

func = [f,g,h]
met = ["trapecio","simpson"]
n = [[130,7],[130,7],[233,9]]
label = ["A","B","C"]

print("                 LAB 5 - EJERCICIO 4\n")

for i in range(0,3):
    print(f"Inciso {label[i]}:\n")
    for j in range(0,2):
        x = intenumcomp(func[i],0,1,n[i][j],met[j])
        print(f"     Regla compuesta de {met[j]} con {n[i][j]} intervalos: {x}\n")
