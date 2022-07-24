def inewton(x,y,z):
	def diff_div():
		c = [[] for i in range(0,len(y))]
		c[0] = y
		for i in range(1,len(y)):
			for j in range(0,len(y)-i):
				c[i].append((c[i-1][j+1]-c[i-1][j])/(x[i+j]-x[j]))
		return [c[i][0] for i in range(0,len(y))]
	
	def prod(t,i):
		r = 1
		for j in range(0,i):
			r *= (t-x[j])
		return r
	
	def p(t,c):
		r = 0
		for i in range(0,len(y)):
			r += c[i]*prod(t,i)
		return r

	c = diff_div()
	w = [p(zi,c) for zi in z]
	return w
	
def test():
	x = [123,342,324,45]
	y = [1,2,3,4]
	z = [5,6,7]
	print(inewton(x,y,z))
	
test()
