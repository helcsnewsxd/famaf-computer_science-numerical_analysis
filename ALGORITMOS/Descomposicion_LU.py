# Triangulares

import numpy as np

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
	
# Descomposicion LU

from scipy.linalg import *

def sollu(A,b):
	P,L,U = lu(A)
	return soltrsup(U,soltrinf(L,np.transpose(P) @ b))

def test():
	A3 = np.array([
		[4,-1,0,-1,0,0],
		[-1,4,-1,0,-1,0],
		[0,-1,4,0,0,-1],
		[-1,0,0,4,-1,0],
		[0,-1,0,-1,4,-1],
		[0,0,-1,0,-1,4]
	],dtype="float")
	b3 = np.array([1,1,1,0,123,0],dtype="float")
	print(f"{A3 @ sollu(A3,b3)} = {b3}")

test()
