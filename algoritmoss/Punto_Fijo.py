def ripf(fun,x0,err,mit):
	hx = []
	punto_anterior = x0
	for k in range(0,mit):
		hx.append(fun(punto_anterior))
		if abs(hx[-1]-punto_anterior) < err:
			break
		punto_anterior = hx[-1]
	return hx

def test():
	f = lambda x : 2**(x-1)
	sol = ripf(f,-1,1e-100,10**5)
	print(f"Da {sol[-1]} con valor {f(sol[-1])} con {len(sol)} iteraciones\n")

test()
