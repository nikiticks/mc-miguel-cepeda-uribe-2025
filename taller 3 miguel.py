# 1. Vehículos fabricados por la fábrica Summer

# a) Total de vehículos
colores = 3
lineas = 5
transmisiones = 3
cilindrajes = 2
total_vehiculos = colores * lineas * transmisiones * cilindrajes
print("Total de vehículos:", total_vehiculos)

# b) Nuevos colores
nuevos_colores = 10
total_vehiculos_nuevos_colores = nuevos_colores * lineas * transmisiones * cilindrajes
print("Total de vehículos con nuevos colores:", total_vehiculos_nuevos_colores)

# 2. Placas de automóviles en Colombia

# a) Total de placas
from math import pow
letras = 25
numeros = 10
total_placas = pow(letras, 3) * pow(numeros, 3)
print("Total de placas:", int(total_placas))

# b) Sin repeticiones
from math import comb
total_placas_sin_repeticiones = comb(letras, 3) * comb(numeros, 3)
print("Total de placas sin repeticiones:", total_placas_sin_repeticiones)

# 3. Selección de directiva

personas = 10
total_maneras = personas * (personas - 1) * (personas - 2) * (personas - 3)
print("Total de maneras de seleccionar directiva:", total_maneras)

# 4. Cadenas de 16 bits que empiezan y terminan con 00

bits_intermedios = 12
total_cadenas = pow(2, bits_intermedios)
print("Total de cadenas:", int(total_cadenas))

# 5. Ubicación de libros en la vitrina

from math import factorial

# a) Total de formas de ubicar los libros
libros = 9
total_formas_libros = factorial(libros)
print("Total de formas de ubicar los libros:", total_formas_libros)

# b) Libros en latín juntos
libros_latin = 5
libros_griego = 4
total_formas_libros_juntos = factorial(libros_latin) * factorial(libros_griego)
print("Total de formas de ubicar libros en latín juntos:", total_formas_libros_juntos)

# c) Alternando libros
total_formas_alternando = factorial