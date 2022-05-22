def pow(x,n):
	if n==0:
		return 1
	k = pow(x,int(n/2))
	if n%2 == 0:
		return k*k
	else:
		return k*k*x

def cinco_primeras_potencias(x):
	for i in range(0,5):
		print(pow(x,i))

cinco_primeras_potencias(2)
