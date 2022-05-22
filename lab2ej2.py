import numpy as np
import matplotlib.pyplot as plt
from ej1 import rbisec

def graphic(function,point_list,x_range,graphic_title):
    def graphic_points(range_x,point_count):
        point_list = [[],[]]

        interval = (range_x[1]-range_x[0])/point_count
        act_point = range_x[0]
        while act_point - range_x[1] < 0:
            point_list[0].append(act_point)
            point_list[1].append(function(act_point))

            act_point = act_point + interval
        
        return point_list


    x = np.linspace(x_range[0],x_range[1],10000)
    fig,ax = plt.subplots()

    [px,py] = graphic_points(x_range,10000)

    ax.plot(px,py,label="Función posta")
    ax.plot(point_list[0],point_list[1],label="Puntos del método usado")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_title(graphic_title)
    ax.legend()
    plt.show()

    return None


def incisoA():
    def fun_lab2ej2a(x):
        return np.tan(x)-2*x
    
    px,py = rbisec(fun_lab2ej2a,[0.8,1.4],1e-5,100)

    print(f"Luego de {len(px)} iteraciones, llegamos a que una aproximación de la menor solución positiva a 2x = tan(x) es {px[-1]}\n")

    graphic(fun_lab2ej2a, [px,py], [0.8,1.4], "Función A")

    return px[-1]


def incisoB():
    def fun_lab2ej2b(x):
        return x**2 - 3
    
    px,py = rbisec(fun_lab2ej2b,[0,3],1e-5,10000)

    print(f"Luego de {len(px)} iteraciones, llegamos a que una aproximación de la menor solución positiva a x = sqrt(3) es {px[-1]}\n")

    graphic(fun_lab2ej2b, [px,py], [0,3], "Función B")

    return px[-1]
