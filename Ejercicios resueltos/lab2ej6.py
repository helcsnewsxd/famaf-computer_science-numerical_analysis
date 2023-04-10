from math import pow
from ej5 import ripf

def convergence_ripf():
    def fun_lab2ej6(x):
        return pow(2,x-1)

    convergence_points = []
    divergence_points = []

    for i in range(-10**4,100):
        j = 2*i/99
        hx = ripf(fun_lab2ej6,j,1e-5,100)
        if len(hx) < 100:
            convergence_points.append([j,hx[-1]])
        else:
            divergence_points.append(j)
    
    print(f"Tenemos entonces que converge para los puntos:\n{convergence_points}\n")
    print(f"Mientras que diverge para:\n{divergence_points}\n")

    return None


print(f"Usando convergence_ripf para analizar la función, llegamos a que esta converge a un valor para (-inf,2] pero para los demás, no (o al menos no se puede asegurar)\n")
