from graphic_function import graphic
from lab3ej1 import ilagrange
from lab3ej2 import inewton
from scipy.interpolate import interp1d

x_interpol = [-3,-2,-1,0,1,2,3]
y_interpol = [1,2,5,10,5,2,1]

x = []
for i in range(0,3):
	x.append([-3+6*i/999 for i in range(0,1000)])

y = []
y.append(ilagrange(x_interpol,y_interpol,x[0]))
y.append(inewton(x_interpol,y_interpol,x[1]))

p_spline = interp1d(x_interpol,y_interpol,kind='cubic',fill_value='extrapolate')
y_spline = p_spline(x[2])
y.append(y_spline)

graphic(x,y,["lagrange","newton","splines"],"Comparación de los diferentes métodos de interpolación",True,0,[True]*3)
