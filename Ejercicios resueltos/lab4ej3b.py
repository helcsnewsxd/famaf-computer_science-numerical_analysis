from graphic_function import graphic
import numpy as np

def input():
	data = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos3b.dat')
	return data[0,1:],data[1,1:]

# y = x/(Ax+B)
# (Ax+B)/x = 1/y
# A+B/x = 1/y
	# Considerando
		# nx = 1/x
		# ny = 1/y
	# entonces
		# A + B * nx = ny

# NOTAR QUE EL PRIMER VALOR ESTÁ AISLADO Y ME PERTURBA MUCHO LA APROXIMACIÓN
# POR ESO, SE DECIDIÓ SACARLO

x,y = input()

nx,ny = np.divide(1,x),np.divide(1,y)

p = np.polyfit(nx,ny,1)

A,B = p[1],p[0]

graphic([x]*2,[y,np.divide(x,A*x+B)],["Datos","Ajuste lineal"],"Ajuste lineal con modelo f(x) = x/(Ax+B)",True,1,[False,True])
