import  cmath 
import  matplotlib.pyplot  as plt
import  numpy as np4

def bairstow(a,r,s,g,roots):
	if(g<1):
		return None
	if((g==1) and (a[1]!=0)):
		roots.append(float(-a[0])/float(a[1]))
		return None
	if(g==2):
		D = (a[1]**2.0)-(4.0)*(a[2])*(a[0])
		X1 = (-a[1] - cmath.sqrt(D))/(2.0*a[2])
		X2 = (-a[1] + cmath.sqrt(D))/(2.0*a[2])
		roots.append(X1)
		roots.append(X2)
		return None
	n = len(a)
	b = [0]*len(a)
	c = [0]*len(a)
	b[n-1] = a[n-1]
	b[n-2] = a[n-2] + r*b[n-1]
	i = n - 3
	while(i>=0):
		b[i] = a[i] + r*b[i+1] + s*b[i+2]
		i = i - 1
	c[n-1] = b[n-1]
	c[n-2] = b[n-2] + r*c[n-1]
	i = n - 3
	while(i>=0):
		c[i] = b[i] + r*c[i+1] + s*c[i+2]
		i = i - 1
	Din = ((c[2]*c[2])-(c[3]*c[1]))**(-1)
	r = r + (Din)*((c[2])*(-b[1])+(-c[3])*(-b[0]))
	s = s + (Din)*((-c[1])*(-b[1])+(c[2])*(-b[0]))
	if(abs(b[0])>1E-14 or abs(b[1])>1E-14):
		return bairstow(a,r,s,g,roots)
	if (g>=3):
		Dis = ((-r)**(2.0))-((4.0)*(1.0)*(-s))
		X1 = (r - (cmath.sqrt(Dis)))/(2.0)
		X2 = (r + (cmath.sqrt(Dis)))/(2.0)
		roots.append(X1)
		roots.append(X2)
		return bairstow(b[2:],r,s,g-2,roots)	


with open("entrada.txt","r") as archivo_entrada:
    entrada = archivo_entrada.read().split("\n")

# Coeficientes del polinomio: 

roots = []
entrada_coef = list(map(float,entrada[1].split()))
print(entrada_coef)
g = int(entrada[0])
r = -1
s = r
bairstow(entrada_coef[::-1],r,s,g,roots)
print("\nFound  Roots => \n")
for r in  roots:
    print("R" + " = " +str(r))


with open("salida.txt","w")as salida:  
    salida.write("POLINOMIO: ")
    for i, x in enumerate(entrada_coef):
        if i == len(entrada_coef)-1:
            salida.write(f"{x}")
            break
        salida.write(f"{x}x^{int(entrada[0])-i} + ")
    salida.write(f"\nRaices: {roots}")

#entradas de prueba

    """
4
1 -2.5 0 2 -4 

3
1 0 -2 1

4
1 0 0 0 -1

5
1 0 5 0 -2 0

3
2.56 3.58 0 6

3
1 0 1 -7 
    """