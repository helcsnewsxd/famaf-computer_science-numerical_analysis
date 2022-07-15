import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import linprog

A_ub = np.array([
    [50,24],
    [30,33]
],dtype="float")
b_ub = np.array([2400,2100],dtype="float")
c = np.array([-1,-1],dtype="float")

res = linprog(c,A_ub,b_ub)
print(f"El maximo de la funcion es {-res.fun} y se obtiene en ({res.x[0]}, {res.x[1]})\n")
print("Respecto al grafico de la region, tenemos:\n")

x = np.linspace(0,40,2000)
y = [(2400-50*x)/24, (2100-30*x)/33]
fig,ax = plt.subplots()
ax.plot(x,y[0])
ax.plot(x,y[1])
ax.plot(res.x[0],res.x[1],'o',label="Maximo")
ax.fill_between(x,np.minimum(y[0],y[1]),alpha=0.6)
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_title("Ejercicio 2 - Region factible")
ax.grid()
ax.legend()
plt.show()