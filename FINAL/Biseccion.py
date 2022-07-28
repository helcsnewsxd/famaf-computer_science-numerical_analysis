import numpy as np

def rbisec(fun,I,err,mit):
	hx,hf = [],[]
	a,b = I[0],I[1]
	sign_fa = np.sign(fun(a))
	
	for k in range(0,mit):
		hx.append((a+b)/2)
		hf.append(fun(hx[-1]))
		
		if abs(hf[-1]) < err:
			break
		
		if sign_fa * np.sign(hf[-1]) < 0:
			b = hx[-1]
		else:
			a = hx[-1]
	
	return (hx,hf)
	
def test():
	f = lambda x : 2*x-np.tan(x)+np.e**5-1235*x**2
	I = [0,2323]
	sol = rbisec(f,I,1e-9,10**6)
	print(f"Da {sol[0][-1]} con un valor de {sol[1][-1]} = {f(sol[0][-1])} usando {len(sol[0])} iteraciones\n")
	
# test()
