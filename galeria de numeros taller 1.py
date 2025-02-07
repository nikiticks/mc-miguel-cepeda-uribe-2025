import random

while True:

    cardinalidad1 = int(input("Ingrese la cardinalidad del primer conjunto: "))
    cardinalidad2 = int(input("Ingrese la cardinalidad del segundo conjunto: "))

    conjunto1 = set(random.randint(0, 30) for _ in range(cardinalidad1))
    conjunto2 = set(random.randint(0, 30) for _ in range(cardinalidad2))

    print("Conjunto 1:", conjunto1)
    print("Conjunto 2:", conjunto2)

    union = conjunto1 | conjunto2
    interseccion = conjunto1 & conjunto2
    diferencia1 = conjunto1 - conjunto2
    diferencia2 = conjunto2 - conjunto1
    diferencia_simetrica = conjunto1 ^ conjunto2

    print("Unión:", union)
    print("Intersección:", interseccion)
    print("Diferencia (A - B):", diferencia1)
    print("Diferencia (B - A):", diferencia2)
    print("Diferencia Simétrica:", diferencia_simetrica)

