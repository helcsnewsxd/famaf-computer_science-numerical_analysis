import numpy as np
from scipy.optimize import linprog

c = np.array([-7,-4,-3])
A_ub = np.array([
    [1,2,2],
    [2,1,2]
])
b_ub = np.array([30,45])

res = linprog(c,A_ub,b_ub)

print(f"Para tener la venta maxima, la cual es de {-res.fun}, debo hacer {res.x[0]} cervezas rubias, {res.x[1]} cervezas negras y {res.x[2]} cervezas de baja graduacion\n")