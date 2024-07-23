# PARTE GENERAL

# Ejercicio A

import numpy as np

def intenumcomp(fun,a,b,N,regla):
    if b <= a:
        return 0

    N = int(np.ceil(N))

    dist = (b-a)/N
    ret = 0
    if regla == "trapecio":
        x = np.linspace(a,b,N+1)
        for xi in x:
            ret += fun(xi)
        ret = dist * (ret*2 - fun(a) - fun(b))/2
    elif regla == "pm":
        x = np.linspace(a+dist/2,b-dist/2,N)
        for xi in x:
            ret += fun(xi)
        ret *= dist
    elif regla == "simpson":
        x = np.linspace(a,b,2*N+1)
        mul = 1
        for xi in x:
            ret += mul*fun(xi)
            if mul == 1:
                mul = 2
            else:
                mul = 1
        ret = dist * (ret*2 - fun(a) - fun(b))/6
    else:
        print("Regla inválida")
        
    return ret
    
L,a,c,h = 20,5,6,3
integral = lambda y : np.sqrt(1-(y/c)**2)
f = lambda h : 2*L*a*intenumcomp(integral,-c,h,11,"pm")
print(f"EJERCICIO A --> Si el nivel de líquido en el tanque es {h}, entonces hay, aproximadamente, {f(h)} m**3 de volumen de combustible\n")

# Ejercicio B

igual = 700/(2*L*a)
ini,fin = -c,3
ans = ini
while ini < fin:
	mid = (ini+fin)/2
	calc = intenumcomp(integral,-c,mid,11,"pm")
	if calc > igual:
		fin = mid
	else:
		ini = mid
	if(abs(calc-igual)<1e-9):
		ans = mid
		break
print(f"EJERCICIO B --> Si tengo 700 m**3, el nivel de líquido en el tanque es de {ans}\n")

# PARTE LIBRE

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


def gs_vs_jac(tol):
	A = np.array([
		[4, -1, 0, -1, 0, 0],
		[-1, 4, -1, 0, -1, 0],
		[0, -1, 4, 0, 0, -1],
		[-1, 0, 0, 4, -1, 0],
		[0, -1, 0, -1, 4, -1],
		[0, 0, -1, 0, -1, 4]
	],dtype="float")
	b = np.array([1,2,3,4,5,6],dtype="float")
	x1 = gseidel(A,b,tol,10**6)
	x2 = jacobi(A,b,tol,10**6)
	print(f"EJERCICIO LIBRE --> TOL = {tol}")
	print(f"Gauss-Seidel: {x1[0]} con {x1[1]} iteraciones")
	print(f"Jacobi: {x2[0]} con {x2[1]} iteraciones")
	return None

gs_vs_jac(1e-100)
