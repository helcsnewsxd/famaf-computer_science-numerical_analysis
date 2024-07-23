import numpy as np
from scipy.optimize import linprog

c = np.array([
    [68.3*52,69.5*212,71*25,71.2*60,68.3*57,69.5*218,71*23,71.2*57,68.3*51,69.5*201,71*26,71.2*54,68.3*56,69.5*223,71*21,71.2*55]
])
A_ub = np.array([
    [52,212,25,60,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,57,218,23,57,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,51,201,26,54,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,56,223,21,55]
])
b_ub = np.array([220,300,245,190])
A_eq = np.array([
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0],
    [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
    [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1]
])
b_eq = np.ones(4)

asig = ["M1","N1","P1","Q1","M2","N2","P2","Q2","M3","N3","P3","Q3","M4","N4","P4","Q4"]
sol = linprog(c,A_ub,b_ub,A_eq,b_eq)
print(f"Para realizar el menor costo posible (${sol.fun} aprox), se debe hacer la siguiente asignacion de tareas:\n")
for i in range(0,4):
    k = []
    for j in range(0,4):
        k.append(sol.x[i+j*4])
    print(asig[np.argmax(k)*4+i])
