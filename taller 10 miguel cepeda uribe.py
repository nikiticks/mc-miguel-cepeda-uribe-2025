import math

# Función para calcular la expansión de la serie de Taylor hasta tercer orden
def taylor_series_f1(x):
    # Definición de la función y sus derivadas para el primer caso
    f_x = 0.3 * x**3 - 1.8 * x**2 + 2.5 * x - 1
    f_prime_x = 0.9 * x**2 - 3.6 * x + 2.5
    f_double_prime_x = 1.8 * x - 3.6
    f_triple_prime_x = 1.8
    
    # Expansión de la serie de Taylor hasta tercer orden
    taylor_approx = f_x + f_prime_x * (0.5 - 0.4) + (f_double_prime_x / 2) * (0.5 - 0.4)**2 + (f_triple_prime_x / 6) * (0.5 - 0.4)**3
    return taylor_approx

def taylor_series_f2(x):
    # Definición de la función y sus derivadas para el segundo caso
    f_x = 1.4 * math.exp(x) - 3.2 * x + 2.4
    f_prime_x = 1.4 * math.exp(x) - 3.2
    f_double_prime_x = 1.4 * math.exp(x)
    f_triple_prime_x = 1.4 * math.exp(x)
    
    # Expansión de la serie de Taylor hasta tercer orden
    taylor_approx = f_x + f_prime_x * (0.65 - 0.6) + (f_double_prime_x / 2) * (0.65 - 0.6)**2 + (f_triple_prime_x / 6) * (0.65 - 0.6)**3
    return taylor_approx

# Resultados de las predicciones
f1_approx = taylor_series_f1(0.4)
f2_approx = taylor_series_f2(0.6)

# Mostrar resultados
print(f"Predicción de f(0.5) para f(x) = 0.3x^3 - 1.8x^2 + 2.5x - 1: {f1_approx}")
print(f"Predicción de f(0.65) para f(x) = 1.4e^x - 3.2x + 2.4: {f2_approx}")
