# EJERCICIO A

from Integrales import intenumcomp

def integral_simpson(x):
	f = lambda y : 1/y
	return intenumcomp(f,1,x,100,"simpson")


# EJERCICIO B

# Notemos que int_1^x (1/y)dy = [ln(y)]_1^x = ln(y)-ln(1) = ln(y)
# Luego, entonces buscamos la raíz de f(x) = ln(y) - 1, la cual es continua en (0,inf)
# Por ello, como [2,4] está en (0,inf), f(2)*f(4) < 0 y se cumplen las condiciones de continuidad para la
# aplicación del método de bisección, sabemos que este va a converger a la solución por Teorema.
# Luego, el método utilizado va a ser el mencionado.

from Biseccion import rbisec

f = lambda x : integral_simpson(x)-1
puntos_visitados = rbisec(f,[2,4],1e-6,100)
aprox_e = puntos_visitados[0][-1]
print(f"EJERCICIO B\n	La aproximación de e obtenida mediante el uso de bisección en [2,4] con tolerancia 1e-6 y máximo 100 iteraciones, es {aprox_e} y haciendo solo {len(puntos_visitados[0])} iteraciones")


# EJERCICIO C

from Graficos import graphic
import numpy as np
import math

print(f"\nEJERCICIO C\n	El error absoluto de la aproximación considerada es de {abs(aprox_e-math.e)}")

x = np.linspace(1,8,1000)

graphic([x,puntos_visitados[0]],[f(x),puntos_visitados[1]],["f(x) = integral_simpson(x)-1","Puntos visitados por Bisección"],"Ejercicio C",True,0,[True,False])
