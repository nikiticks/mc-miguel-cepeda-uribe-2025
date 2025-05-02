import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Datos
X = np.array([
    [1, 0],
    [1, 0.5],
    [2, 0.5],
    [3, 1],
    [-1.5, -1.2],
    [2, 1.5],
    [3, 1.5],
    [3, 0.5]
])
y = np.array([0.2, 3, -0.8, -0.4, 3.5, 3.6, 0.5, -1])

# Modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Predicciones
y_pred = model.predict(X)

# Coeficiente de determinación R^2
r2 = r2_score(y, y_pred)

# Coeficiente de correlación de Pearson
correlation_matrix = np.corrcoef(y, y_pred)
correlation = correlation_matrix[0, 1]

# Resultados
print("Coeficientes: ", model.coef_)
print("Intercepto: ", model.intercept_)
print("R^2 (Coeficiente de determinación): ", r2)
print("Coeficiente de correlación: ", correlation)

# Gráfica
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], y, color='blue', label='Datos reales')
ax.scatter(X[:, 0], X[:, 1], y_pred, color='red', label='Predicción')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.set_title('Regresión lineal múltiple')
ax.legend()
plt.show()
