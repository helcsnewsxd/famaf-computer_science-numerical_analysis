import numpy as np
from scipy.linalg import *

def jacobi(A,b,err,mit):
	x = [np.zeros(len(b)),np.zeros(len(b))]
	M = np.diag(np.diag(A))
	N = -(A-M)
	M_inv = inv(M)
	M_inv_x_N = M_inv @ N
	it = 0
	for k in range(0,mit):
		it+=1
		x[0] = x[1]
		x[1] = M_inv_x_N @ (x[0]) + M_inv @ b
		if norm(x[1]-x[0],np.inf) <= err:
			break
	return [x[1],it]


def test():
	A = np.array([
		[3, 1, 1],
		[2, 6, 1],
		[1, 1, 4]
	],dtype="float")
	b = np.array([5,9,6],dtype="float")
	sol = jacobi(A,b,1e-11,10**6)
	print(f"{A @ sol[0]} = {b} con {sol[1]} iteraciones")

test()
