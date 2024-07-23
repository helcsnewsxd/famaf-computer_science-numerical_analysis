import numpy as np

def soltrinf(A,b):
    x = []
    x.append(b[0]/A[0][0])
    for i in range(1,len(b)):
        x.append((b[i] - sum([x[j]*A[i][j] for j in range(0,i)]))/A[i][i])
    return np.array(x)

def soltrsup(A,b):
    x = []
    x.append(b[-1]/A[-1][-1])
    for i in range(1,len(b)):
        i2 = len(b)-1-i
        x.append((b[i2] - sum(x[j]*A[i2][len(b)-1-j] for j in range(0,i)))/A[i2][i2])
    x2 = [x[len(b)-1-i] for i in range(0,len(b))]
    return np.array(x2)
