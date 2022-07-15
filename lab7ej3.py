import numpy as np
from scipy.optimize import linprog
from matplotlib import pyplot as plt

# maximizar z = 25x + 20y
#   sujeto a 3x + 4y <= 25
#            2x + y <= 10

A_ub = np.array([
    [3,4],
    [2,1]
],dtype="float")
b_ub = np.array([25,10],dtype="float")
c = np.array([-25,-20],dtype="float")

res = linprog(c,A_ub,b_ub)
print(f"Para obtener {-res.fun} puntos de salud, conviene hacer {res.x[0]} unidades de Med1 y {res.x[1]} unidades de Med2\n")
print("El grafico del conjunto factible es el siguiente:\n")
x = np.linspace(0,6,1000)
y = [(25-3*x)/4, 10-2*x]
fig,ax = plt.subplots()
ax.plot(x,y[0],label="Restriccion de hierba A")
ax.plot(x,y[1],label="Restriccion de hierba B")
ax.plot(res.x[0],res.x[1],'o',label="Maximo")
ax.fill_between(x,np.maximum(0,np.minimum(y[0],y[1])),0)
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_title("Ejercicio 3 - Region Factible")
ax.grid()
ax.legend()
plt.show()