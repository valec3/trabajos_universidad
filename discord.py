contador = 0
acumulador = 0
mayor = 59
menor = 61
print("Bienvenido a los juegos del hambre")
for n in range (1,25):
  prueba=int(input("Ingrese la velocidad del fluido de cada prueba."))
  acumulador=acumulador + prueba
  if prueba > mayor:
    mayor = prueba
  else:
    if prueba < menor:
      menor = prueba
      contador=contador + 1
promedio = acumulador / 25
print("El promedio de las velocidades es: ", promedio)
print("Hubieron ", contador, "valores por debajo de 60.")
print("el valor mayor fue: ", mayor, "y el valor menor fue: ", menor)