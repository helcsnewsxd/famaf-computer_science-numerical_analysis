#f(x) = sqrt(x^2+1)-1

#g(x) = x^2 / (sqrt(x^2+1)+1)

#veamos que
#f(x) = g(x)
#sqrt(x^2+1)-1 = x^2 / (sqrt(x^2+1)+1)
#(sqrt(x^2+1)-1) * sqrt(x^2+1)+1) = x^2
#(sqrt(x^2+1))^2-1 = x^2
#x^2+1-1 = x^2
#x^2 = x^2 --> Luego, se muestra la igualdad

from math import sqrt

def f(x):
	return sqrt(x*x+1)-1
	
def g(x):
	return x*x/(sqrt(x*x+1)+1)

for i in range(20):
	x = 8**-i
	print(f"f(x)={f(x)}, g(x)={g(x)}")
	
#ambas funciones devuelven numeros distintos y la mas confiable es g(x) ya que no presenta resta, la unica operacion peligrosa que debemos procurar obviar
