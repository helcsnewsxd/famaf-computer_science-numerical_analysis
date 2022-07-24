# Se considera aproximacion por un modelo polinomial de grado n
# Si es un modelo diferente, debe llevarse a la forma polinomial o, en caso que las x estén afectadas
# por funciones, se ponen tal cual en la matriz

import numpy as np
from scipy.linalg import *

def cuad_min(x,y,n):
	AT = [x**(n-j) for j in range(0,n+1)]
	B = y
	A = np.transpose(AT)
	sol = solve(AT @ A, AT @ B)
	return sol

import matplotlib.pyplot as plt

def test():
	x = np.array([-1,0,1,3,6])
	y = np.array([6.1,2.8,2.2,6,26.9])
	n = 2
	coef = cuad_min(x,y,n)
	print(f"Coeficientes --> {coef}")
	f = lambda x : coef[0]*x**2 + coef[1]*x + coef[2]
	print(f"Datos --> {y}")
	print(f"Aproximacion --> {f(x)}")
	err = 0
	for i in range(0,len(y)):
		err += (y[i]-f(x[i]))**2
	print(f"Error --> {err}")
	plt.plot(x,y,'o')
	plt.plot(np.linspace(-2,7,1000),f(np.linspace(-2,7,1000)))
	plt.grid()
	plt.show()

test()
