import numpy as np
import matplotlib.pyplot as plt

# Datos
X = np.array([0, 1, 2, 3, 4, 5, 6, 7])
Y = np.array([7.5, 5.5, 6.5, 3.5, 4.5, 3, 2.5, 1])

# Cálculo de los coeficientes de la recta (m, b) usando mínimos cuadrados
m, b = np.polyfit(X, Y, 1)

# Predicción
Y_pred = m * X + b

# Visualización
plt.scatter(X, Y, label="Datos", color="blue")
plt.plot(X, Y_pred, label=f"Ajuste: y = {m:.2f}x + {b:.2f}", color="red")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("Regresión Lineal por Mínimos Cuadrados")
plt.show()
