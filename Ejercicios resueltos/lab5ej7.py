from lab5ej1 import intenumcomp
from numpy import e
import time

def simpson_adaptativo(fun,a,b,err):
    aprox = 0
    stack = [[a,b,err,intenumcomp(fun,a,b,2,"simpson")]]
    while stack:
        act = stack.pop()
        act_a, act_b, act_err, act_q = act[0], act[1], act[2], act[3]
        act_c = (act_a+act_b)/2
        act_q1, act_q2 = intenumcomp(fun,act_a,act_c,2,"simpson"), intenumcomp(fun,act_c,act_b,2,"simpson")

        if abs(act_q - act_q1 - act_q2) < 15*act_err:
            aprox += act_q1 + act_q2
        else:
            stack.append([act_a,act_c,act_err/2,act_q1])
            stack.append([act_c,act_b,act_err/2,act_q2])
    return aprox


print("                     LAB 5 - EJERCICIO 7\n")

f = lambda x : x * e**(-x**2)
a = 0
b = 1
err = 1e-15

tmp = []

aprox_exacta = 1/2*(1-1/e)

time_ini = time.time()
aprox_smp_adap = simpson_adaptativo(f,a,b,err)
time_fin = time.time()
tmp.append(time_fin-time_ini)

time_ini = time.time()
aprox_smp_comp = intenumcomp(f,a,b,3118,"simpson")
time_fin = time.time()
tmp.append(time_fin-time_ini)

print("Comparaciones con error menor a 1e-15:\n")
print(f"    Valor exacto: {aprox_exacta}\n")
print(f"    Aprox simpson adaptativa: {aprox_smp_adap} con {tmp[0]} segundos de tiempo\n")
print(f"    Aprox simpson compuesta: {aprox_smp_comp} con {tmp[1]} segundos de tiempo y 3118 intervalos\n")