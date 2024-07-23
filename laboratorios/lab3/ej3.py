from ej2 import inewton
from graphic_function import graphic

def f(x):
	return 1/x

x_interpol = range(1,6)
y_interpol = [f(xi) for xi in x_interpol]

x = [[24/25 + j/25 for j in range(1,102)]]
y = [[f(xi) for xi in x[0]]]

x.append(x[0])
y.append(inewton(x_interpol,y_interpol,x[1]))

graphic(x,y,["f(x)","p(x)"],"f(x)=1/x y su polinomio interpolante p(x) en [1,5]",True,0,[True]*2)
