import random

def generar_vector(longitud):
    return [random.randint(1, 100) for _ in range(longitud)]

def producto_escalar(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def main():
    try:
        n = int(input("Introduce la longitud de los vectores (entero positivo): "))
        if n <= 0:
            print("Por favor, introduce un número entero positivo.")
            return

        vector1 = generar_vector(n)
        vector2 = generar_vector(n)

        print("Vector 1:", vector1)
        print("Vector 2:", vector2)

        resultado = producto_escalar(vector1, vector2)
        print("El producto escalar de los vectores es:", resultado)

    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")

if __name__ == "__main__":
    main()
