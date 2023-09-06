import math
# Ingrese los coeficientes de la ecuación cuadrática
A = float(input("Ingrese el coeficiente A: "))
B = float(input("Ingrese el coeficiente B: "))
C = float(input("Ingrese el coeficiente C: "))
# Calcular el discriminante (D)
D = B**2 - 4*A*C
# Calcular las soluciones de la ecuación
if D > 0:
    # Dos soluciones reales distintas
    x1 = (-B + math.sqrt(D)) / (2*A)
    x2 = (-B - math.sqrt(D)) / (2*A)
    print("Las soluciones son:")
    print("x1 =", x1)
    print("x2 =", x2)
elif D == 0:
    # Una solución real única
    x1 = -B / (2*A)
    print("La solución única es:")
    print("x1 =", x1)
else:
    # Soluciones complejas
    realPart = -B / (2*A)
    imaginaryPart = math.sqrt(-D) / (2*A)
    print("No tiene soluciones reales y las soluciones complejas son:")
    print(f"x1 = {realPart} + {imaginaryPart}i")
    print(f"x2 = {realPart} - {imaginaryPart}i")
