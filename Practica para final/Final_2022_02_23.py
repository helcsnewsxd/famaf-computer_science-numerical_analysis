import numpy as np

# EJERCICIO 1

	# Funciones pre-hechas

def soltrsup(A,b):
    x = []
    x.append(b[-1]/A[-1][-1])
    for i in range(1,len(b)):
        i2 = len(b)-1-i
        x.append((b[i2] - sum(x[j]*A[i2][len(b)-1-j] for j in range(0,i)))/A[i2][i2])
    x2 = [x[len(b)-1-i] for i in range(0,len(b))]
    return np.array(x2)

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


def rbisec(fun,I,err,mit):
    def sig_distinct(x,y):
        return (x < 0 and y > 0) or (x > 0 and y < 0)

    point_list = ([],[])

    left,right = I[0],I[1]
    fleft,fright = fun(left),fun(right)
    dist = right-left

    if not sig_distinct(fleft, fright):
        print("El intervalo dado no cumple las hipótesis para aplicar el método de la bisección\n")
        return point_list

    for i in range(1,mit-1):
        dist = dist/2
        half = left+dist
        fhalf = fun(half)

        point_list[0].append(half)
        point_list[1].append(fhalf)

        if abs(fhalf) < err:
            break

        if sig_distinct(fleft, fhalf):
            right,fright = half,fhalf
        else:
            left,fleft = half,fhalf
    
    return point_list

	# Realizacion del ejercicio

A = np.array([
	[3,1,1],
	[1,3,1],
	[1,1,3]
],dtype="float")
B = np.array([1,1,1],dtype="float")
X = soleg(A,B)
f = lambda w : w**3 - 10*w**2 + 10*w + 1 - X[0]
X[0] = rbisec(f,[8,10],10**-9,10**6)[0][-1]
print(f"EJERCICIO 1\nLa solucion es la siguiente: {X[0],X[1],X[2]}\n")


# EJERCICIO PARA LIBRES

					# ~ Super	Deluxe		Stock
	# ~ Kg brasilero	0.5		0.25		120
	# ~ Kg colombiano	0.5		0.75		160
	# ~ Ganancia p/kg	22		30

from scipy.optimize import linprog
A = np.array([
	[0.5,0.25],
	[0.5,0.75]
],dtype="float")
B = np.array([120,160],dtype="float")
c = np.array([22,30],dtype="float")
sol = linprog(-c,A,B).x
print(f"EJERCICIO LIBRE\nHay que hacer {sol[0]} kg de Cafe Super y {sol[1]} kg de Cafe Deluxe\n")
