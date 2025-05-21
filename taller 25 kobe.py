x = [0, 1, 2, 3, 4, 5]
y = [0, 5, 2.5, 4, -1.6, 2]
x_objetivo = 3.55

def lagrange(x, y, x_val):
    total = 0
    n = len(x)
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (x_val - x[j]) / (x[i] - x[j])
        total += term
    return total

def linear_interpolation(x, y, x_val):
    for i in range(len(x) - 1):
        if x[i] <= x_val <= x[i + 1]:
            # Spline lineal entre x[i] y x[i+1]
            t = (x_val - x[i]) / (x[i+1] - x[i])
            return y[i] + t * (y[i+1] - y[i])
    return None

resultado_lagrange = lagrange(x, y, x_objetivo)
resultado_lineal = linear_interpolation(x, y, x_objetivo)

print(f"Resultado con Lagrange en x = {x_objetivo}: {resultado_lagrange:.4f}")
print(f"Resultado con interpolación lineal (como spline básico) en x = {x_objetivo}: {resultado_lineal:.4f}")
