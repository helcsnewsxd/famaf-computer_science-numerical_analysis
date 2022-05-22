def horn(coefs,x):
	retorno = 0
	for k in coefs:
		retorno = retorno * x + k
	return retorno

p = horn([1,-5,6,2],2)
print(p)
