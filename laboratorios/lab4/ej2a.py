from graphic_function import graphic
import numpy as np

def f(x):
	return np.arcsin(x)

x = [i/49 for i in range(0,50)]
y = [f(xi) for xi in x]

for n in range(0,6):
	p = np.polyfit(x,y,n)
	err = 0
	for i in range(0,len(x)):
		err += (y[i]-np.polyval(p,x[i]))**2
	print(f"El error del modelo de grado {n} es igual a {err}\n")
	graphic([x]*2,[y,[np.polyval(p,xi) for xi in x]],["Datos",f"Ajuste de grado {n}"],"Ajuste de f(x) = arcsen(x) en [0,1] por distintos grados",n==5,n+1,[False,True])
