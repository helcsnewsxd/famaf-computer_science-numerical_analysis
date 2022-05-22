from graphic_function import graphic
import numpy as np

def input():
	data = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos1a.dat')
	return data[:,0] , data[:,1]

x,y = input()
m = len(x)
one = np.ones(m)

coef = np.linalg.solve([[m,x.dot(one)],[x.dot(one),x.dot(x)]],[y.dot(one),x.dot(y)])
f = lambda x:coef[1]*x+coef[0]

graphic([x,[x[0],x[-1]]],[y,[f(x[0]),f(x[-1])]],["Puntos","Ajuste"],"Ajuste lineal por minimos cuadrados discreto",True,0,[False,True])
