from ej3 import rnewton

def circunference_diameter(E,V):
    def function(x):
        return E-0.01328 * x**2 * V**3 , -2 * 0.01328 * x * V**3
    
    px,py = rnewton(function,E,1e-10,10**7)

    return px[-1]
