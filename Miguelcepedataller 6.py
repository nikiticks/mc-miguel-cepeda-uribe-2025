import math

def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def taylor_cos(x, tol=0.5 * 10**-8):
    
    term = 1  # Primer término de la serie
    cos_x = term  # Valor inicial de coseno
    n = 1  # Contador de iteraciones
    
    while True:
        prev_cos_x = cos_x
        term = (-1) ** n * (x ** (2 * n)) / factorial(2 * n)
        cos_x += term
        
        # Cálculo del error relativo aproximado
        error_a = abs((cos_x - prev_cos_x) / cos_x) * 100
        
        if error_a < tol:
            break
        
        n += 1
    
    return cos_x, error_a, n

# Entrada del usuario
x = float(input("Ingrese el valor en radianes: "))
cos_x, error_a, iteraciones = taylor_cos(x)

# Resultados
print(f"Coseno aproximado: {cos_x}")
print(f"Error relativo aproximado: {error_a:.8f}%")
print(f"Número de iteraciones: {iteraciones}")
