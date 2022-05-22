from lab3ej2 import inewton
from graphic_function import graphic
from numpy import cos
from numpy import pi

def f(x):
	return 1/(1+25 * x**2)

def do_graphic_with_grade(n,b):
	xp_interpol = [2*(i-1)/n-1 for i in range(1,n+2)]
	yp_interpol = [f(xi) for xi in xp_interpol]

	xq_interpol = [cos((2*i+1)/(2*n+2)*pi) for i in range(0,n+1)]
	yq_interpol = [f(xi) for xi in xq_interpol]

	x = [[-1+2*i/199 for i in range(0,200)]]*3
	y = [[f(xi) for xi in x[0]]]

	y.append(inewton(xp_interpol,yp_interpol,x[0]))
	y.append(inewton(xq_interpol,yq_interpol,x[0]))

	graphic(x,y,["f(x)","p(x)","q(x)"],f"f(x) y sus dos polinomios interpolantes. Puntos equidistantes vs. nodos de Tchebychev. Ejemplo con grado n = {n}",b,n,[True]*3)
	return None

for ni in range(1,16):
	do_graphic_with_grade(ni,ni==15)
