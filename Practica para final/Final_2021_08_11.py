# EJERCICIO 1

import numpy as np

def rfalsi(f,I,err,mit):
	hx,hf=[],[]
	a,b = I[0],I[1]
	for i in range(0,mit):
		fa,fb = f(a),f(b)
		hx.append((fb*a-fa*b)/(fb-fa))
		hf.append(f(hx[-1]))
		if abs(f(hx[-1])) < err:
			break
		if np.sign(fa)*np.sign(hf[-1]) < 0:
			a = hx[-1]
		else:
			b = hx[-1]
	return (hx,hf)

# EJERCICIO 2

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

f = lambda x : x**3 - 10*x**2 + 10*x + 1
rbisec_sol = rbisec(f,[7,11],1e-5,100)
rfalsi_sol = rfalsi(f,[7,11],1e-5,100)
print(f"EJERCICIO 1\nBiseccion --> {rbisec_sol[0][-1]} con {len(rbisec_sol[0])} iteraciones\n")
print(f"Falsa Posicion --> {rfalsi_sol[0][-1]} con {len(rfalsi_sol[0])} iteraciones\n")
print("Gana Falsa Posicion\n")

# EJERCICIO LIBRE

from graphic_function import graphic
f = lambda x : np.sign(x-1)*np.sqrt(abs(x-1))
x = np.linspace(0,2,1000)
graphic([x],[[f(xi) for xi in x]],["Funcion"],"Ejercicio Libre - Inciso A",True,0,[True])

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

def f2(x):
	return f(x),np.sign(x-1)*1/(2*np.sqrt(abs(x-1)))

print("EJERCICIO LIBRE\n")
rnewton_solve = rnewton(f2,1.00001,10**-9,100)
print(f"Diverge y rnewton da f({rnewton_solve[0][-1]}) = {rnewton_solve[1][-1]}\n")
