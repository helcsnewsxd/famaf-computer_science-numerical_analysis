def rnewton(fun,x0,err,mit):
	hx,hf = [],[]
	
	faux = fun(x0)
	punto_anterior = x0
	f_punto_anterior = faux[0]
	df_punto_anterior = faux[1]
	
	for k in range(0,mit):
		hx.append(punto_anterior-f_punto_anterior/df_punto_anterior)
		faux = fun(hx[-1])
		hf.append(faux[0])
		
		if abs(hx[-1]-punto_anterior)/abs(hx[-1]) < err or abs(hf[-1]) < err:
			break
		
		punto_anterior = hx[-1]
		f_punto_anterior = hf[-1]
		df_punto_anterior = faux[1]
	
	return (hx,hf)

def test():
	a = 12233.23434
	f = lambda x : (x**3 - a, 3*x**2)
	sol = rnewton(f,a,1e-15,10**9)
	print(f"Da {sol[0][-1]} con valor {sol[1][-1]} = {f(sol[0][-1])[0]}\n")

test()
