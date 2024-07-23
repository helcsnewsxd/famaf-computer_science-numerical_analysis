def horn(coefs,x):
	p = 0
	for i in range(0,len(coefs)-1):
		p = (p+coefs[i])*x
	p += coefs[-1]
	return p

def test():
	f = lambda x : 10*x**5+1234*x**4-35*x**3-4356*x**2+0*x+93
	x = 123.13
	coefs = [10,1234,-35,-4356,0,93]
	print(f"{horn(coefs,x)} --- {f(x)}")

test()
