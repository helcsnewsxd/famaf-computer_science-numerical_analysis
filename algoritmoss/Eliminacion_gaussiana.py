# Triangulares

def soltrinf(A,b):
	x = np.array(b)
	for i in range(0,len(b)):
		for j in range(0,i):
			x[i]-=A[i][j]*x[j]
		x[i]/=A[i][i]
	return x

def soltrsup(A,b):
	x = np.array(b)
	n = len(b)
	f = lambda x : n-1-x
	for i in range(0,n):
		for j in range(0,i):
			x[f(i)]-=A[f(i)][f(j)]*x[f(j)]
		x[f(i)]/=A[f(i)][f(i)]
	return x

# Eliminacion Gaussiana

def egauss(A,b):
	U = np.array(A)
	y = np.array(b)
	for i in range(0,len(b)):
		for j in range(i+1,len(b)):
			coef = U[j][i]/U[i][i]
			for q in range(i,len(b)):
				U[j][q]-=coef*U[i][q]
			y[j]-=coef*y[i]
	return [U,y]

def soleg(A,b):
	sist = egauss(A,b)
	return soltrsup(sist[0],sist[1])


import numpy as np

def test():
	A = np.array([
		[2,0,0,0,0],
		[2,34,0,0,0],
		[12,-123.3,23.123,0,0],
		[1,0,0,123.12345,0],
		[0.123,123.456,1.23,4,-123.5]
	],dtype="float")
	b = np.array([1,2,3,4,5],dtype="float")
	print(f"{A @ soltrinf(A,b)} = {b}")
	
	AT = np.transpose(A)
	b2 = np.array([5,4,3,2,1],dtype="float")
	print(f"{AT @ soltrsup(AT,b2)} = {b2}")
	
	A3 = np.array([
		[4,-1,0,-1,0,0],
		[-1,4,-1,0,-1,0],
		[0,-1,4,0,0,-1],
		[-1,0,0,4,-1,0],
		[0,-1,0,-1,4,-1],
		[0,0,-1,0,-1,4]
	],dtype="float")
	b3 = np.array([1,1,1,0,12,0],dtype="float")
	print(f"{A3 @ soleg(A3,b3)} = {b3}")

test()
