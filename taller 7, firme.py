def a_complemento_a_dos(n):
    if n < 0:
        n = (1 << 16) + n
    return n

def de_complemento_a_dos(n):
    if n & (1 << 15):
        n -= (1 << 16)
    return n

def suma_binaria(a, b):
    a_bin = a_complemento_a_dos(a)
    b_bin = de_complemento_a_dos(b)
    result_bin = (a_bin + b_bin) & 0xFFFF
    return de_complemento_a_dos(result_bin)

num1 = int(input("Introduce el primer número entero (entre -32768 y 32767): "))
num2 = int(input("Introduce el segundo número entero (entre -32768 y 32767): "))
resultado = suma_binaria(num1, num2)
print("La suma es:", resultado)
