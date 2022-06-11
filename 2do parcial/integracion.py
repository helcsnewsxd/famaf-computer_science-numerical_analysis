# Modificación del método del trapecio para integrar funciones en intervalos de longitud arbitraria
# La idea es considerar que en cada caso se suma (y[i]+y[i+1])/2 * (x[i+1]-x[i])
    # Sin embargo, se plantea sumar siempre en cada iteración cosas del mismo signo de modo que se
    # disminuya la cantidad de restas de nros de distinto signo quedando en, finalmente, solo una
    # Lo mismo se hace con la división. La idea es disminuir la cantidad de operaciones realizadas

def trapecio_adaptativo(x,y):
    suma, resta = [0,0],[0,0]
    for i in range(0,len(x)-1):
        aux = [(y[i]+y[i+1])*x[i+1] , (y[i]+y[i+1])*x[i]]
        suma[aux[0] > 0] += aux[0]
        resta[aux[1] > 0] += aux[1]
    return ((suma[0]+suma[1])-(resta[0]+resta[1]))/2