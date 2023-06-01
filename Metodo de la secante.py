import math,os
def metodo_secante(x_0,x_1,f,tol,pasos):
    raices=[x_0,x_1]
    x_n=0
    error = 1
    n=0
    errores = [None,None]
    while error > tol:
        n+=1
        x_n = x_0 - ( (x_1 - x_0) / (f(x_1) - f(x_0)) ) * f(x_0)
        raices.append(x_n)
        error = abs(f(x_n))
        errores.append(error)
        if f(x_n) == 0:
            return raices,errores
        x_0 = x_1
        x_1 = x_n
        if n > pasos:
            return raices,errores
    return raices,errores

f = lambda x: x**2 -3*x +2 

raices,errores = metodo_secante(0,1,f,1e-9,50)
os.system("cls")
print("-"*17)
for i,r in enumerate(raices):
    print(f"|x_{i} | {r:f}\t|{errores[i]}")
print("-"*17)
print(f"f(x_6)={f(raices[-1])}\n")