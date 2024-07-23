def rbisec(fun,I,err,mit):
    def sig_distinct(x,y):
        return (x < 0 and y > 0) or (x > 0 and y < 0)

    point_list = ([],[])

    left,right = I[0],I[1]
    fleft,fright = fun(left),fun(right)
    dist = right-left

    if not sig_distinct(fleft, fright):
        print("El intervalo dado no cumple las hipótesis para aplicar el método de la bisección\n")
        return point_list

    for i in range(1,mit-1):
        dist = dist/2
        half = left+dist
        fhalf = fun(half)

        point_list[0].append(half)
        point_list[1].append(fhalf)

        if abs(fhalf) < err:
            break

        if sig_distinct(fleft, fhalf):
            right,fright = half,fhalf
        else:
            left,fleft = half,fhalf
    
    return point_list


def testing_rbisec(I):
    def example_function(x):
        return x**3-1
    
    px,py = rbisec(example_function,I,1e-100,10**8)
    print(f"Luego de {len(px)} iteraciones, llegamos a que una raíz de la función es {px[-1]}\n")
    print(f"Para testear, miremos los puntos medios:\n- Valor en X: {px}\n- Valor en Y: {py}\n")

    return (px[-1],py[-1])