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
