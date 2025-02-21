import math
def combinaciones(n, k):
    return math.comb(n, k)
aplicaciones_totales = 20
aplicaciones_seleccionadas = 8
seleccion_aplicaciones = combinaciones(aplicaciones_totales, aplicaciones_seleccionadas)


redes_sociales_totales = 6
redes_sociales_seleccionadas = 3
otras_aplicaciones_totales = 14
otras_aplicaciones_seleccionadas = 5

seleccion_redes_sociales = combinaciones(redes_sociales_totales, redes_sociales_seleccionadas)
seleccion_otras_aplicaciones = combinaciones(otras_aplicaciones_totales, otras_aplicaciones_seleccionadas)
seleccion_total = seleccion_redes_sociales * seleccion_otras_aplicaciones


cartas_totales = 52
cartas_seleccionadas = 5
manos_poker = combinaciones(cartas_totales, cartas_seleccionadas)


palos = 4
cartas_palo = 13
manos_mismo_palo = palos * combinaciones(cartas_palo, cartas_seleccionadas)


denominaciones_totales = 13
cartas_tres_misma_denominacion = combinaciones(denominaciones_totales, 1) * combinaciones(4, 3)
cartas_dos_misma_denominacion = combinaciones(denominaciones_totales - 1, 1) * combinaciones(4, 2)
manos_poker_tres_dos = cartas_tres_misma_denominacion * cartas_dos_misma_denominacion


print("1a. Selección de aplicaciones:", seleccion_aplicaciones)
print("1b. Selección de aplicaciones específicas:", seleccion_total)
print("2a. Manos de póker:", manos_poker)
print("2b. Manos de póker del mismo palo:", manos_mismo_palo)
print("2c. Manos de póker con tres y dos cartas de diferentes denominaciones:", manos_poker_tres_dos)
