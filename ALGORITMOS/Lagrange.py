def ilagrange(x,y,z):
	def l(i,t):
		r = 1
		for j in range(0,len(y)):
			if j == i:
				continue
			r *= (t-x[j])/(x[i]-x[j])
		return r
	
	def p(t):
		r = 0
		for i in range(0,len(y)):
			r += y[i]*l(i,t)
		return r
	
	w = [p(zi) for zi in z]
	return w

def test():
	x = [123,342,324,45]
	y = [1,2,3,4]
	z = [5,6,7]
	print(ilagrange(x,y,z))
	
test()
