def f(x, y):
    return x**2 + y**2 - 1

def g(x, y):
    return x**2 - y

def punto_fijo(x0, y0, tolerance, max_iterations):
    x = x0
    y = y0
    
    for _ in range(max_iterations):
        x_next = g(x, y)
        y_next = f(x, y)
        
        if abs(x_next - x) < tolerance and abs(y_next - y) < tolerance:
            return x_next, y_next
        
        x = x_next
        y = y_next
    
    return None

# Valores iniciales
x0 = 0.5
y0 = 0.5

# Tolerancia y máximo de iteraciones
tolerance = 1e-6
max_iterations = 100

# Resolución del sistema de ecuaciones no lineales
solution = punto_fijo(x0, y0, tolerance, max_iterations)

if solution is not None:
    x, y = solution
    print("Solución encontrada:")
    print("x =", x)
    print("y =", y)
else:
    print("No se pudo encontrar una solución en las iteraciones máximas.")
