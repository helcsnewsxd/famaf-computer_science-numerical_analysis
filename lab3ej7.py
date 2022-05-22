from bhaskara import bhaskara
from lab3ej1 import ilagrange

# Es una muy buena opción para calcular raíces ya que tiene mejor performance que los
# otros métodos que vimos
# Sin embargo, un problema grave es que puede suceder que el polinomio cuadrático interpolante q2 no tenga raíces

def rinterp(fun,x0,x1,x2,err,mit):
	def aabs(x):
		if(x < 0):
			x *= -1
		return x

	def coef(r):
		c = r[1]
		r[0] -= c
		r[2] -= c
		a = (r[0]+r[2])/2
		b = r[2]-a
		return [a,b,c]

	for it in range(0,mit):
		if(aabs(fun(x2))<err):
			break

		r,k = bhaskara(coef(ilagrange([x0,x1,x2],[fun(x0),fun(x1),fun(x2)],[-1,0,1])))

		if(k):
			print("El q2 no tiene raíces")
			break

		if(aabs(r[0]-x2) < aabs(r[1]-x2)):
			x0=x1
			x1=x2
			x2=r[0]
		else:
			x0=x1
			x1=x2
			x2=r[1]
	return x2
