from graphic_function import graphic
import numpy as np

def input():
	data = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos1a.dat')
	return data[:,0] , data[:,1]

def precalculo(x,y):
	sumas = [0 for i in range(0,4)]
	for i in range(0,len(x)):
		sumas[0] += x[i]
		sumas[1] += x[i]**2
		sumas[2] += x[i]*y[i]
		sumas[3] += y[i]
	return sumas

def coef_pol_aprox(sumas,m):
	a = m*sumas[2] - sumas[0]*sumas[3]
	a /= m*sumas[1] - sumas[0]**2

	b = sumas[1]*sumas[3] - sumas[2]*sumas[0]
	b /= m*sumas[1] - sumas[0]**2
	return a,b


x,y = input()
sumas = precalculo(x,y)
a,b = coef_pol_aprox(sumas,len(x))
f = lambda x:a*x+b


graphic([x,[x[0],x[-1]]],[y,[f(x[0]),f(x[-1])]],["Puntos","Ajuste"],"Ajuste lineal discreto por mínimos cuadrados",True,0,[False,True])
