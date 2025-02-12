while True:
    def solicitar_conjunto(nombre):
        cardinalidad = int(input(f"Ingrese la cardinalidad del conjunto {nombre}: "))
        conjunto = set(input(f"Ingrese los elementos del conjunto {nombre} separados por espacios: ").split())
        return conjunto


    def verificar_subconjunto(U, A):
        return A.issubset(U)


    def operar_conjuntos(U, A):
        operacion1 = (U.intersection(A)).union(A)
        operacion2 = U - (A.intersection(A))
        operacion3 = (U.symmetric_difference(A)) - A
        return operacion1, operacion2, operacion3


    U = solicitar_conjunto("U")
    A = solicitar_conjunto("A")


    if verificar_subconjunto(U, A):
        operacion1, operacion2, operacion3 = operar_conjuntos(U, A)
        print(f"(U ⋂ A) ⋃ A: {operacion1}")
        print(f"U - (A ⋂ A): {operacion2}")
        print(f"(U ⨁ A) - A: {operacion3}")
    else:
        print