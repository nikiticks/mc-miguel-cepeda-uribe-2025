import numpy as np

# Definimos los puntos base
puntos_base = np.array([
    [1, 3],
    [3, 0],
    [5, -1],
    [7, 2.5],
    [9, 1]
])

def lagrange_interpolacion(x_eval, puntos):
    """
    Implementa la interpolación de Lagrange para calcular f(x_eval)
    basado en los puntos proporcionados.
    """
    n = len(puntos)
    resultado = 0
    
    for i in range(n):
        xi, yi = puntos[i]
        termino = yi
        
        for j in range(n):
            if i != j:
                xj = puntos[j][0]
                termino *= (x_eval - xj) / (xi - xj)
        
        resultado += termino
    
    return resultado

# Valores estimados para f(4.25) con grados 1, 2 y 3
grados = [1, 2, 3]
x_valor = 4.25

for grado in grados:
    puntos_usados = puntos_base[:grado+1]  # Tomamos los primeros (grado+1) puntos
    estimacion = lagrange_interpolacion(x_valor, puntos_usados)
    print(f"Estimación de f({x_valor}) con polinomio de grado {grado}: {estimacion:.5f}")