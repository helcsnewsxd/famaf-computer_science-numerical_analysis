from graphic_function import graphic
import numpy as np

def input():
	data = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos3a.dat')
	return data[0],data[1]

# y = Cx^A
# ln y = ln C + A * ln x

# Luego, si tenemos que
	# ny = ln y
	# nx = ln x
	# nC = ln C
# nos queda que: ny = nC + A * nx

x,y = input()
nx = np.log(x)
ny = np.log(y)

p = np.polyfit(nx,ny,1)

A = p[0]
C = np.exp(p[1])

f = lambda x : C * x ** A

graphic([x]*2,[y,[f(xi) for xi in x]],["Datos","Ajuste Lineal"],"Ajuste lineal por modelo y(x) = C*x^A",True,0,[False,True])
