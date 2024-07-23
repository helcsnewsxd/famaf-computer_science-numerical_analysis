import numpy as np
from ej5 import *

print("         EJERCICIO 6         \n")

A = np.array([
    [3, 1, 1],
    [2, 6, 1],
    [1, 1, 4]
],dtype="float")
b = np.array([5,9,6],dtype="float")
print("CASO 1\n")
print(f"    Jacobi: {jacobi(A,b,10**-11,1e10)}\n")
print(f"    Gseidel: {gseidel(A,b,10**-11,1e10)}\n\n")

A = np.array([
    [5, 7, 6, 5],
    [7, 10, 8, 7],
    [6, 8, 10, 9],
    [5, 7, 9, 10]
],dtype="float")
b = np.array([22,32,33,31],dtype="float")
print("CASO 2\n")
print(f"    Jacobi: {jacobi(A,b,10**-4,782)} --> DIVERGE\n")
print(f"    Gseidel: {gseidel(A,b,10**-4,1e10)}\n\n")