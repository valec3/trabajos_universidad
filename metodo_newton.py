def newton_raphson_method(f, f_prime, initial_guess, tolerance, max_iterations):
    x_prev = initial_guess
    
    print("Iteración\tAproximación")
    
    for i in range(max_iterations):
        f_val = f(x_prev)  # Calcula el valor de la función en el punto previo
        f_prime_val = f_prime(x_prev)  # Calcula el valor de la derivada de la función en el punto previo
        
        x = x_prev - f_val / f_prime_val  # Calcula la próxima aproximación utilizando la fórmula de Newton-Raphson
        
        print(f"{i+1}\t\t{x}")
        if abs(x - x_prev) < tolerance:
            return x  # Se encontró una aproximación satisfactoria
        
        
        x_prev = x  # Actualiza el valor previo
    
    print("No se encontró una aproximación satisfactoria después de", max_iterations, "iteraciones.")
    return None

# Ejemplo de uso
def f(x):
    return x**2 - 2  # Función f(x) utilizada para encontrar la raíz

def f_prime(x):
    return 2*x  # Derivada de la función f(x)

initial_guess = 2  # Valor inicial de la aproximación
tolerance = 0.0001  # Tolerancia para la aproximación
max_iterations = 10  # Máximo número de iteraciones

approximation = newton_raphson_method(f, f_prime, initial_guess, tolerance, max_iterations)
if approximation is not None:
    print("Aproximación:", approximation)
