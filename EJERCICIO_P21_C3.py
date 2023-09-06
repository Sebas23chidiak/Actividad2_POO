# se le pide al usuario  que ingrese los tres lados del triángulo
la1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
la2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
la3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))
# Calcular el perímetro del triángulo
perimetro = la1 + la2 + la3
# Calcular el semiperímetro del triángulo
semiperimetro = perimetro / 2
# Calcular el área del triángulo usando la fórmula de Herón
s = semiperimetro  # Semiperímetro
area = (s * (s - la1) * (s - la2) * (s - la3)) ** 0.5
# Mostrar los resultados
print("\nResultados:")
print("El perímetro del triángulo es:", perimetro)
print("El semiperímetro del triángulo es:", semiperimetro)
print("El área del triángulo es:", area)
