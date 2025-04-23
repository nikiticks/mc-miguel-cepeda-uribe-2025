import numpy as np

# Datos de entrada
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1.5, 2.5, 3.5, 4.5, 6.5, 9])

# Paso 1: Aplicar el logaritmo natural a los valores de y
y_log = np.log(y)

# Paso 2: Realizar la regresión lineal sobre x y ln(y)
# Calculamos la pendiente (b) y la intersección (C) usando la fórmula de regresión lineal
# y = b * x + C
n = len(x)
sum_x = np.sum(x)
sum_y_log = np.sum(y_log)
sum_xx = np.sum(x * x)
sum_xy_log = np.sum(x * y_log)

# Calculamos la pendiente (b) y la intersección (C) de la recta
b = (n * sum_xy_log - sum_x * sum_y_log) / (n * sum_xx - sum_x**2)
C = (sum_y_log - b * sum_x) / n

# Paso 3: Obtener los valores de 'a' y 'b'
a = np.exp(C)  # a = e^C

# Mostrar los resultados
print(f"Coeficiente a (e^C): {a}")
print(f"Coeficiente b: {b}")

# El modelo final es: y = a * exp(b * x)
def modelo_exponencial(x_val):
    return a * np.exp(b * x_val)

# Probar el modelo con los datos originales
predicciones = modelo_exponencial(x)

print("\nPredicciones del modelo exponencial:")
for i in range(len(x)):
    print(f"x = {x[i]}, Predicción = {predicciones[i]}, Real = {y[i]}")
