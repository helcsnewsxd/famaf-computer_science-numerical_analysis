def inewton(x,y,z):
	def diff_div():
		c = [[yi] for yi in y]
		for j in range(1,len(x)):
			for i in range(0,len(x)-j):
				c[i].append((c[i+1][j-1]-c[i][j-1])/(x[i+j]-x[i]))
		return c

	def p(k,C):
		suma = 0
		prod = 1
		for i in range(0,len(x)):
			suma += prod*C[0][i]
			prod *= k-x[i]
		return suma

	C = diff_div()
	return [p(zi,C) for zi in z]
