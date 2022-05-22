def ilagrange(x,y,z):
	def l(i,k):
		prod = 1
		for j in range(0,len(x)):
			if(i!=j):
				prod *= (k-x[j])/(x[i]-x[j])
		return prod

	def p(k):
		suma = 0
		for i in range(0,len(x)):
			suma += y[i]*l(i,k)
		return suma

	return [p(zi) for zi in z]
