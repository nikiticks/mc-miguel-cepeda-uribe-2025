import random
import numpy as np

def generar_dimensiones():
    filas_a = random.randint(2, 8)
    columnas_a = random.randint(2, 8)
    filas_b = columnas_a  # Para que la multiplicación sea válida
    columnas_b = random.randint(2, 8)
    return (filas_a, columnas_a), (filas_b, columnas_b)

def generar_matriz(filas, columnas):
    return np.random.randint(1, 101, size=(filas, columnas))

def main():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Multiplicación")
    operacion = input("Introduce 1 o 2: ")

    if operacion not in {"1", "2"}:
        print("Operación no válida. Elige 1 o 2.")
        return

    if operacion == "1":
        filas, columnas = random.randint(2, 8), random.randint(2, 8)
        matriz_a = generar_matriz(filas, columnas)
        matriz_b = generar_matriz(filas, columnas)

        print("Matriz A:\n", matriz_a)
        print("Matriz B:\n", matriz_b)
        resultado = matriz_a + matriz_b
        print("Resultado de la suma:\n", resultado)

    elif operacion == "2":
        dims_a, dims_b = generar_dimensiones()
        matriz_a = generar_matriz(*dims_a)
        matriz_b = generar_matriz(*dims_b)

        print("Matriz A:\n", matriz_a)
        print("Matriz B:\n", matriz_b)
        resultado = np.dot(matriz_a, matriz_b)
        print("Resultado de la multiplicación:\n", resultado)

if __name__ == "__main__":
    main()
