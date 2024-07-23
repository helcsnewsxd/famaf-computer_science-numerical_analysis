from graphic_function import graphic
import numpy as np

def f(x):
	return 3/4*x-1/2

x = [10*i/19 for i in range(0,20)]
y = [f(xi) for xi in x]

ny = [yi+np.random.randn() for yi in y]

p = np.polyfit(x,ny,1)

graphic([x]*4,[y,[np.polyval(p,xi) for xi in x],ny,y],["Original","Ajuste de perturbada","Datos perturbados","Datos originales"],"Visión del método de cuadrados mínimos",True,0,[True,True,False,False])
