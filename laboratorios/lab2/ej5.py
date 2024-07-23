def ripf(fun,x0,err,mit):
    point_list = []

    before,f_before = x0,fun(x0)
    point_list.append(before)

    for i in range(1,mit-1):
        now = fun(before)
        point_list.append(now)

        if abs(now-before) < err:
            break
            
        before = now
    
    return point_list


def testing_ripf(x0):
    def example_function(x):
        return (x**2 - 1)/3 #un ejemplo del teórico
    
    px = ripf(example_function,x0,1e-10,10**9)

    return px[-1]