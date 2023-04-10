from ej1 import rbisec
from ej3 import rnewton
from ej5 import ripf
import numpy as np
import matplotlib.pyplot as plt

def graphic(point_list,x_range):
    x = np.linspace(x_range[0],x_range[1],10000)
    fig,ax = plt.subplots()

    ax.plot(point_list[0],point_list[1])
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_title("Gráfico aproximado")
    ax.legend()
    plt.show()

    return None

def lab2ej7bisec():
    point_list = ([],[])
    for i in range(0,148):
        x = i/99
        def u(y):
            return y-np.e**(-(1-x*y)**2)
        
        px,py = rbisec(u,[-100,100],1e-10,10**7)
        point_list[0].append(x)
        point_list[1].append(px[-1])
    
    graphic(point_list, [0,1.5])

    return None


def lab2ej7newton():
    point_list = ([],[])
    for i in range(0,148):
        x = i/99
        def u(y):
            return y-np.e**(-(1-x*y)**2),1 - np.e**(-(1-x*y)**2) * 2*(1-x*y)*y
        
        px,py = rnewton(u, x, 1e-10, 10**7)
        point_list[0].append(x)
        point_list[1].append(px[-1])
    
    graphic(point_list, [0,1.5])

    return None


def lab2ej7ipf():
    point_list = ([],[])
    for i in range(0,148):
        x = i/99
        def u(y):
            return np.e**(-(1-x*y)**2)
        
        px = ripf(u, 0, 1e-10, 10**4)
        point_list[0].append(x)
        point_list[1].append(px[-1])
    
    graphic(point_list, [0,1.5])

    return None
