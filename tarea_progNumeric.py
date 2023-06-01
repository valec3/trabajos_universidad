import math
def biseccion(f, x_i, x_u, tol=1e-6):
    """
    Encuentra la raíz de la función f en el intervalo [a,b]
    usando el método de bisección con una tolerancia dada.
    """
    conteo=0
    fx_i = f(x_i)
    fx_u = f(x_u)
    #Paso 1
    if fx_i * fx_u > 0:
        print("La función debe tener signos opuestos en los extremos del intervalo.")

    while (x_u - x_i) / 2 > tol:
        #Paso 2
        #Aproximacion de la raiz
        x_r = (x_i + x_u) / 2
        fx_r = f(x_r)
        conteo+=1
        print(f"Paso: {conteo} \t{x_i:.4f} \t{x_u:.4f} \t{x_r:.4f} \t{f(x_r):.4f}\t   {(x_u - x_i) / 2 }")
        
        #Paso 3
        #caso x_r)
        if fx_r == 0:
            return x_r
        #caso a)
        elif fx_i * fx_r < 0:
            x_u = x_r
            # fx_u = fc
        #caso b)
        else:
            x_i = x_r
            fx_i = fx_r
    
        if conteo>30:
                break
    x_r = (x_i + x_u) / 2
    print(f"Paso: {conteo+1} \t{x_i:.4f} \t{x_u:.4f} \t{x_r:.4f} \t{f(x_r):.4f}\t   {(x_u - x_i) / 2 }")
    return x_r

def bisection(fun, x_a, x_b, eps=None, steps=10):
    # The bisection method cannot be applied
    if fun(x_a) * fun(x_b) >= 0:
        print("The bisection method cannot be applied")
        return None
    
    # Calculate number of stepds base on eps
    if eps is not None:
        steps = math.ceil(math.log((x_b - x_a) / eps) / math.log(2))
    
    # The bisection method
    for n in range(steps + 1):
        x_m = (x_a + x_b) / 2
        print(f"Paso: {n+1} \t{x_a:.4f} \t{x_b:.4f} \t{x_m:.4f} \t{f(x_m):.4f}")
        if f(x_m) == 0:
            return x_m
        
        if f(x_a) * f(x_m) < 0:
            x_b = x_m
        else:
            x_a = x_m
    
    return (x_a + x_b) / 2

def bisection(fun, xl, xu, tol):
    if fun(xl) * fun(xu) > 0:
        print("El método de bisección no se puede aplicar en este intervalo.")
        return None
    xm = (xl + xu) / 2
    while abs(fun(xm)) > tol:
        if fun(xl) * fun(xm) < 0:
            xu = xm
        else:
            xl = xm
        xm = (xl + xu) / 2
    return xm


#----FUNCIONES

def f(x):
    return x**3 - 2*x - 5
def f_2(x):
    return (667.38/x)*(1-pow(math.e,-0.146843*x))-40
def f_3(x):
    return pow(x,3) + 4 * pow(x,2) - 10
def f_4(x):
    return 4*x**2 - 5*x
def f_5(x):
    return pow(math.e,3*x) - 4

print("Pasos  \t\tx_i \tx_u \tx_r \tf(x_r) \tError")
print("."*57)
print("La raiz es: ",biseccion(f_5,0,1,0.01) )
