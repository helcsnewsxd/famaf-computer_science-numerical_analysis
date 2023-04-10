import numpy as np
from scipy.integrate import quad as intenum

def pendulo(l,a):
    g = 9.8
    a = a*np.pi/180
    f = lambda x : 1 / (1-np.sin(a/2)**2 * np.sin(x)**2)**(1/2)
    (integral,err) = intenum(f,0,np.pi/2)

    T = 4 * np.sqrt(l/g) * integral

    return T