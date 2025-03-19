import math

def calcular_error(f_derivada, x_aprox, delta_x):
    return abs(f_derivada(x_aprox)) * delta_x

def f1(x):
    return 1.1 * x**4 - 1.9 * x**3 + 1.2 * x**2 - 2 * x + 4

def f1_derivada(x):
    return 4.4 * x**3 - 5.7 * x**2 + 2.4 * x - 2

def f2(x):
    return math.cos(x) * math.log(2 * x)

def f2_derivada(x):
    return -math.sin(x) * math.log(2 * x) + (math.cos(x) / x)

x1_aprox = 1.4
delta_x1 = 0.05

x2_aprox = math.pi / 3
delta_x2 = 0.005

error_resultante1 = calcular_error(f1_derivada, x1_aprox, delta_x1)
error_resultante2 = calcular_error(f2_derivada, x2_aprox, delta_x2)

print(f"Error resultante para la primera función: {error_resultante1}")
print(f"Error resultante para la segunda función: {error_resultante2}")
