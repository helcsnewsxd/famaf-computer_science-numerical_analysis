import numpy as np
from scipy.linalg import *

def jacobi(A,b,err,mit):
    k = 0
    x = [np.zeros(len(b))]*2
    M = np.diag(np.diag(A))
    Minv = inv(M)
    Minv_x_N = Minv @ (-(A-M))

    while k < mit:
        x[0] = x[1]
        x[1] = Minv_x_N @ x[0] + Minv @ b

        k+=1
        if norm(x[1]-x[0], ord=np.inf) <= err:
            break
    
    return [x[1],k]

def gseidel(A,b,err,mit):
    k = 0
    x = [np.zeros(len(b))]*2
    M = np.tril(A)
    Minv = inv(M)
    Minv_x_N = Minv @ (-(np.triu(A)-np.diag(np.diag(A))))

    while k < mit:
        x[0] = x[1]
        x[1] = Minv_x_N @ x[0] + Minv @ b

        k+=1
        if norm(x[1]-x[0], ord=np.inf) <= err:
            break
    
    return [x[1],k]
