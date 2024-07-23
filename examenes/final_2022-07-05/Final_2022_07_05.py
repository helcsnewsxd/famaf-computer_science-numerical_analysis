# EJERCICIO 1A

def rnewtondelta(fun,x0,err,mit,delta):
    hx,hf=[x0],[fun(x0)]
    for i in range(0,mit):
        aprox_derivada = (fun(hx[-1]+delta)-hf[-1])/delta
        hx.append(hx[-1]-hf[-1]/aprox_derivada)
        hf.append(fun(hx[-1]))
        if abs(hf[-1])<err or (abs(hx[-1]-hx[-2])/abs(hx[-1]))<err:
            break
    return (hx,hf)

# EJERCICIO 1B

import numpy as np
from graphic_function import graphic

f = lambda x : np.e**x - x - 2
x = np.linspace(0,10,1000)
graphic([x],[[f(xi) for xi in x]],["e**x - x - 2"],"Ejercicio 1B",True,0,[True])

# EJERCICIO 1C

#   Newton tradicional

def rnewton(fun,x0,err,mit):
    point_list = ([],[])

    before = x0
    f_before,df_before = fun(before)

    point_list[0].append(before)
    point_list[1].append(f_before)

    for i in range(1,mit-1):
        if abs(df_before) < 0: # para no dividir por un nro cercano a 0
            break
        
        now = before - f_before/df_before
        f_now,df_now = fun(now)

        point_list[0].append(now)
        point_list[1].append(f_now)

        if (not(now < err) and abs((now-before)/now) < err) or abs(f_now) < err:
            break
        
        before,f_before,df_before = now,f_now,df_now

    return point_list

print("EJERCICIO 1C\n")
def f2(x):
    return f(x),np.e**x - 1
newton_tradicional = rnewton(f2,1,1e-6,100)
newton_nuevo = (rnewtondelta(f,1,1e-6,100,1e-5),rnewtondelta(f,1,1e-6,100,0.001))
print("Método de Newton tradicional\n")
print(f"Raiz = {newton_tradicional[0][-1]} con {len(newton_tradicional[0])} iteraciones\n\n")
print("Método de Newton nuevo\n")
print(f"Con delta = {1e-5}: Raiz = {newton_nuevo[0][0][-1]} con {len(newton_nuevo[0][0])} iteraciones\n")
print(f"Con delta = {0.001}: Raiz = {newton_nuevo[1][0][-1]} con {len(newton_nuevo[1][0])} iteraciones\n\n")


# EJERCICIO 2

#   Reglas compuestas de integracion

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

print("EJERCICIO 2\n")
f = lambda x : np.sqrt(1-x**2)
ini,fin=1,10000
while ini+1 < fin:
    mid = (ini+fin-(ini+fin)%2)/2
    err = abs(2*intenumcomp(f,-1,1,mid,"simpson")-np.pi)
    if err < 1e-5:
        fin = mid
    else:
        ini = mid
print(f"Se aproxima con {fin} intervalos con Simpson de modo que pi = ")
print(2*intenumcomp(f,-1,1,fin,"simpson"))