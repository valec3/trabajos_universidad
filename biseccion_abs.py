import math
def biseccion(f, x_i, x_u,tol):
    """
    Encuentra la raíz de la función f en el intervalo [x_i,x_u]
    usando el método de bisección con una tolerancia dada.
    """
    conteo=0
    raiz_ant=0
    ea=1
    #Paso 1
    if f(x_i) * f(x_u) > 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo.")
    
    while ea > tol: #criterio de paro
        #Paso 2
        raiz = (x_i + x_u) / 2 #aproximacion de la raiz
        ea=abs((raiz-raiz_ant)/raiz)
        conteo+=1
        fa = f(x_i)
        fb = f(x_u)
        fc = f(raiz)
        print(f"{conteo}\t{x_i:.4f}\t{x_u:.4f}\t{raiz:.4f}\t{f(raiz):.2f}\t{ea:.4f}")
        #Paso 3
        if fa*fc == 0: #c)
            return raiz
        elif fa * fc < 0: #a)
            x_u = raiz
        elif fa * fc > 0: #b)
            x_i = raiz
        raiz_ant =raiz #guardamos la raiz anterior
        if conteo>70:
            break
    return raiz

def f(x):
    return x**3 - x - 1


print("Pasos\tx_i\tx_u\tx_r\tf(x_r)\tError")
print("La Raiz es: ",biseccion(f,1,2,0))