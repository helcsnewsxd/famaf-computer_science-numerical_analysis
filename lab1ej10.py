def SonReciprocos(x,y):
	return x*y == 1

import random
for _ in range(100):
	x = 1+random.random()
	y = 1/x
	if not SonReciprocos(x,y):
		print(x)

#se imprimen varios x ya que cabe la gran posibilidad de que al utilizar random.random(), varios de los nros de x sean representados como nros binarios con cifras periodicas en su parte fraccionaria
#del mismo modo, pasa con y = 1/x, por lo que se produce un error de redondeo y no queda que x*y = 1 pese a que y = 1/x
