from matplotlib import pyplot as plt
from scipy.optimize import linprog
import numpy as np

R_izq = np.array([
    [-3,-2],
    [-1,-3],
    [-8,-2]
],dtype="float")
R_der = np.array([-3,-1.5,-4],dtype="float")
Z = np.array([10,8],dtype="float")

res = linprog(Z,R_izq,R_der)
print("          EJERCICIO 1\n")
print(f"Se deben comprar {res.x[0]}kg de T1 y {res.x[1]}kg de T2 con tal de minimizar el costo total a {res.fun}\n\n")

print("El gráfico saldrá a continuación:\n")
x = np.linspace(0,2,1000)
y = [(3-3*x)/2,(1.5-x)/3,(4-8*x)/2]
fig,ax = plt.subplots()
ax.plot(x,y[0],label="Restriccion P")
ax.plot(x,y[1],label="Restriccion N")
ax.plot(x,y[2],label="Restriccion K")
ax.plot(res.x[0],res.x[1],'o',label="Minimo costo")
ax.fill_between(x,np.maximum(y[0],np.maximum(y[1],y[2])),3,alpha=0.6)
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_title("Ejercicio 1 - Region Factible")
ax.grid()
ax.legend()
plt.show()