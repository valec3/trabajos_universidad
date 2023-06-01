def ruffini(coeficientes, a):
    n = len(coeficientes) - 1
    resultados = coeficientes.copy()
    # Realiza la división sintética
    for i in range(1, n + 1):
        resultados[i] += a * resultados[i - 1]

    # Retorna el cociente y el residuo
    cociente = resultados[:-1]
    residuo = resultados[-1]
    #print("ruf: ",cociente,a,residuo)

    return cociente, residuo


def encontrar_raices(coeficientes):
    raices = []
    a_values = []
    b_values = []
    termino_independiente = coeficientes[-1]

    # Generar posibles raíces enteras (divisores del término independiente)
    if termino_independiente != 0:
        for i in range(1, abs(termino_independiente) + 1):
            if termino_independiente % i == 0:
                a_values.append(i)
                a_values.append(-i)
    print(a_values)

    # Generar posibles raíces racionales (divisores del coeficiente termino indep )
    if coeficientes[0] != 0:
        for i in range(1, abs(coeficientes[0]) + 1):
            if coeficientes[0] % i == 0:
                b_values.append(i)
                b_values.append(-i)

    print(b_values)
    # Aplicar Ruffini con las posibles raíces enteras
    for a in a_values:
        cociente, residuo = ruffini(coeficientes, a)
        if residuo == 0:
            raices.append(a)
            coeficientes = cociente
        if len(coeficientes) == 2:
            raices.append(
                coeficientes[1] / coeficientes[0]
            )
            break
        
    for b in b_values:
        pass
        
    return raices


# Ejemplo de uso
coeficientes = [2, 1 ,-8 ,-1 , 6]  # Polinomio: x^2 - 5x + 6


#
# PEDIR ENTRADA
#

with open("entrada.txt","r") as archivo_entrada:
    entrada = archivo_entrada.read().split("\n")

# Coeficientes del polinomio: 
entrada_coef = list(map(int,entrada[1].split()))
print(entrada_coef)
roots = encontrar_raices(entrada_coef)

print("Las raíces del polinomio son:", roots)

#
#ESCRIBIR SALIDA
#
with open("salida.txt","w")as salida:  
    salida.write("POLINOMIO: ")
    for i, x in enumerate(entrada_coef):
        if i == len(entrada_coef)-1:
            salida.write(f"{x}")
            break
        salida.write(f"{x}x^{int(entrada[0])-i} + ")
    salida.write(f"\nRaices reales {roots}")
    salida.write(f"\nraices complejas complex {roots}")