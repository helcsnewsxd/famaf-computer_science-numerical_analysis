import numpy as np
from ej1 import soltrsup

def egauss(A,b):
    U = np.copy(A)
    y = np.copy(b)

    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            k = U[j][i]/U[i][i]
            for z in range(i+1,len(A)):
                U[j][z] -= U[i][z]*k
            y[j] -= y[i]*k
            U[j][i] = 0
    
    return [U,y]

def soleg(A,b):
    s = egauss(A,b)
    return soltrsup(s[0],s[1])