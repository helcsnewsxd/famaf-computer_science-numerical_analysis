import numpy as np

def intenumcomp(fun,a,b,N,regla):
	aprox = 0
	x = np.linspace(a,b,N+1)
	dist = (b-a)/N
	
	if regla == "rectangulo":
		for i in range(0,len(x)-1):
			aprox += fun(x[i])
		aprox *= dist
			
	elif regla == "trapecio":
		for i in range(1,len(x)-1):
			aprox += 2*fun(x[i])
		aprox = (aprox+fun(x[0])+fun(x[-1]))/2*dist
		
	elif regla == "pm":
		for i in range(0,len(x)-1):
			aprox += fun((x[i]+x[i+1])/2)
		aprox *= dist
	
	elif regla == "simpson":
		for i in range(0,len(x)-1):
			aprox += 4*fun((x[i]+x[i+1])/2)
		for i in range(1,len(x)-1):
			aprox += 2*fun(x[i])
		aprox = (aprox + fun(x[0])+fun(x[-1]))/6 * dist
		
	else:
		assert(False)
	
	return aprox


import numpy as np

def test():
	f = lambda x : np.e**(-x)
	N = 2
	regla = "simpson"
	a = 0
	b = 1
	print(intenumcomp(f,a,b,N,regla))

# test()
