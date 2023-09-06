import math
# Se le pide al usuario que ingrese la longitud del lado del triángulo equilátero
lado = float(input("Ingrese la longitud del lado del triángulo equilátero: "))
# Calcular el perímetro del triángulo equilátero
perimetro = 3 * lado
# Calcular la altura del triángulo equilátero
altura = (math.sqrt(3) / 2) * lado
# Calcular el área del triángulo equilátero
area = (math.sqrt(3) / 4) * lado ** 2
# Mostrar los resultados
print("\nResultados:")
print("Perímetro:", perimetro)
print("Altura:", altura)
print("Área:", area)
