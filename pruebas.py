import math
def biseccion(f, a, b, tol=1e-6):
    """
    Encuentra la raíz de la función f en el intervalo [a,b]
    usando el método de bisección con una tolerancia dada.
    """
    conteo=0
    #Paso 1
    fa = f(a)
    fb = f(b)
    c_a=0
    if fa * fb > 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo.")
    while (b - a) / 2 > tol :
        #Paso 2
        c = (a + b) / 2 #aproximacion de la raiz
        conteo+=1
        fc = f(c)
        print(f"Paso {conteo}:\t{c}  -  {c_a} / 2  =  {(c-c_a)/c}")###extra
        #Paso 3
        if fa*fc == 0:
            return c
        elif abs((c-c_a)/c) < 0.005 :
            break
        elif fa * fc < 0:
            c_a=c
            b = c
            fb = fc
        elif fa * fc > 0:
            c_a=c
            a = c
            fa = fc            
    return c

def biseccion_2(f, a, b, tol=1e-6):
    """
    Encuentra la raíz de la función f en el intervalo [a,b]
    usando el método de bisección con una tolerancia dada.
    """
    conteo=0
    c_a=0
    #Paso 1
    if f(a) * f(b) > 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo.")
    
    while abs((c-c_a)/c) < 0.005 : #criterio de paro
        #Paso 2
        c = (a + b) / 2 #aproximacion de la raiz
        conteo+=1
        fa = f(a)
        fb = f(b)
        fc = f(c)
        print(f"Paso {conteo}:\t{c}  -  {c_a} / {c}  =  {(c-c_a)/c}")###Salida
        #Paso 3
        if fa*fc == 0: #c)
            return c
        elif abs((c-c_a)/c) < 0.005 : #criterio de paro
            print("error absluto")
            break
        elif fa * fc < 0: #a)
            b = c
        elif fa * fc > 0: #b)
            a = c
        c_a =c #guardamos el c anterior
        
        if conteo>30:
            break
    return c

def f(x):
    return x**3 - 2*x - 5
def f_2(x):
    return (667.38/x)*(1-pow(math.e,-0.146843*x))-40
def f_3(x):
    return pow(x,3) + 4 * pow(x,2) - 10

# raiz = biseccion(f, 2, 3)
# print("La raíz de la función es aproximadamente:", raiz)
# print("La raíz de la función es aproximadamente:", round(biseccion(f_2,12,16,0.005),4))
# print("V.2La raíz de la función es aproximadamente:", round(biseccion_2(f_2,12,16,0.005),4))
print("La raiz es: ",biseccion_2(f_3,1,2,pow(10,-4)) )
print("·"*20)

