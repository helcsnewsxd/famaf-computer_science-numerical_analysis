def rnewton(fun,x0,err,mit):
    point_list = ([],[])

    before = x0
    f_before,df_before = fun(before)

    point_list[0].append(before)
    point_list[1].append(f_before)

    for i in range(1,mit-1):
        if abs(df_before) < 0: # para no dividir por un nro cercano a 0
            break
        
        now = before - f_before/df_before
        f_now,df_now = fun(now)

        point_list[0].append(now)
        point_list[1].append(f_now)

        if (not(now < err) and abs((now-before)/now) < err) or abs(f_now) < err:
            break
        
        before,f_before,df_before = now,f_now,df_now

    return point_list

def testing_rnewton(x0):
    def example_function(x):
        return x**3 - 8,3*x**2
    
    (px,py) = rnewton(example_function, x0, 1e-10, 10**6)
    print(f"Luego de {len(px)} iteraciones, llegamos a que una raíz de la función es {px[-1]}\n")
    print(f"Para testear, miremos los puntos por los que pasa:\n- Valor en X: {px}\n- Valor en Y: {py}\n")

    return (px[-1],py[-1])
