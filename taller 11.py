def f(x):
    return 0.25 * x**4 - 0.75 * x**2 + 4.5


x = 0.6
h1 = 0.1
h2 = 0.05


f_primera_centrada_h1 = (f(x + h1) - f(x - h1)) / (2 * h1)
f_segunda_centrada_h1 = (f(x + h1) - 2*f(x) + f(x - h1)) / h1**2
f_primera_centrada_h2 = (f(x + h2) - f(x - h2)) / (2 * h2)
f_segunda_centrada_h2 = (f(x + h2) - 2*f(x) + f(x - h2)) / h2**2

f_prima_exacta = x**3 - 1.5 * x
f_segunda_exacta = 3 * x**2 - 1.5


print("Primera derivada (centrada):")
print(f"Con h = 0.1: {f_primera_centrada_h1}")
print(f"Con h = 0.05: {f_primera_centrada_h2}")
print(f"Verdadero: {f_prima_exacta}")

print("\nSegunda derivada (centrada):")
print(f"Con h = 0.1: {f_segunda_centrada_h1}")
print(f"Con h = 0.05: {f_segunda_centrada_h2}")
print(f"Verdadero: {f_segunda_exacta}")


error_primera_h1 = abs(f_primera_centrada_h1 - f_prima_exacta)
error_primera_h2 = abs(f_primera_centrada_h2 - f_prima_exacta)
error_segunda_h1 = abs(f_segunda_centrada_h1 - f_segunda_exacta)
error_segunda_h2 = abs(f_segunda_centrada_h2 - f_segunda_exacta)

print("\nErrores en la primera derivada:")
print(f"Con h = 0.1: {error_primera_h1}")
print(f"Con h = 0.05: {error_primera_h2}")

print("\nErrores en la segunda derivada:")
print(f"Con h = 0.1: {error_segunda_h1}")
print(f"Con h = 0.05: {error_segunda_h2}")


if error_primera_h2 < error_primera_h1:
    print("\nLa primera derivada es más precisa con h = 0.05.")
else:
    print("\nLa primera derivada es más precisa con h = 0.1.")

if error_segunda_h2 < error_segunda_h1:
    print("La segunda derivada es más precisa con h = 0.05.")
else:
    print("La segunda derivada es más precisa con h = 0.1.")
