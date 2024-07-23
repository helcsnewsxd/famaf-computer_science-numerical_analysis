from ej3 import rnewton

def raiz_cubica(a):
    if not(a>0):
        print("No me cumple la precondición del problema\n")
        return None

    def function(x):
        return x**3 - a,3*x**2

    (px,py) = rnewton(function, a, 1e-6, 10**6)

    return px[-1]
    
print(f'La raíz cúbica de 8 es {raiz_cubica(8)}')