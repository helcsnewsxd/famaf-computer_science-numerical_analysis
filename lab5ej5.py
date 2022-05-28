from scipy.integrate import quad as intenum
import numpy as np

f = lambda x : np.e ** (-x**2)
g = lambda x : x**2 * np.log(x+np.sqrt(x**2 + 1))

func = [f,g]
p = [[-np.inf,np.inf],[0,2]]
label = ["A","B"]

print("             LAB 5 - EJERCICIO 5\n")

for i in range(0,2):
    (x,y) = intenum(func[i],p[i][0],p[i][1])
    print(f"Inciso {label[i]}:\n")
    print(f"    Aprox: {x}\n")
    print(f"    Posible error abs: {y}\n")