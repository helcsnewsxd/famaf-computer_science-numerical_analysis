def SonOrtogonales(x,y):
	return x[0]*y[0] + x[1]*y[1] == 0

x = [1,1.1024074512658109]
y = [-1,1/x[1]]
if not SonOrtogonales(x,y):
	print("Algo salio mal...")

#El error esta dado en que son nros relativamente cercanos y para calcular el producto escalar utilizamos una suma que, dado el valor de y[0], termina siendo una resta de -2 con un valor muy cercano a 2
#Por ello, el error es el que se produce luego de aplicar la resta
