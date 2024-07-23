import numpy as np
from ej2 import soleg
from ej3 import sollu

A = np.array([
    [4, -1, 0, -1, 0, 0],
    [-1, 4, -1, 0, -1, 0],
    [0, -1, 4, 0, 0, -1],
    [-1, 0, 0, 4, -1, 0],
    [0, -1, 0, -1, 4, -1],
    [0, 0, -1, 0, -1, 4]
],dtype="float")
b = [
    np.array([1,1,1,0,0,0],dtype="float"),
    np.ones(6)
]

print("             EJERCICIO 4             \n")
print(f"soleg(A,b1) = {soleg(A,b[0])}\n")
print(f"soleg(A,b2) = {soleg(A,b[1])}\n\n")
print(f"sollu(A,b1) = {sollu(A,b[0])}\n")
print(f"sollu(A,b2) = {sollu(A,b[1])}\n\n")
