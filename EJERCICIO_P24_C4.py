# Ingrese los pesos de las esferas
peso_A = float(input("Ingrese el peso de la esfera A: "))
peso_B = float(input("Ingrese el peso de la esfera B: "))
peso_C = float(input("Ingrese el peso de la esfera C: "))
# Inicializar una variable para almacenar el peso máximo
peso_maximo = 0
# Comparar los pesos de las esferas para encontrar la más pesada
if peso_A > peso_B and peso_A > peso_C:
    peso_maximo = peso_A
    esfera_maxima = "A"
elif peso_B > peso_A and peso_B > peso_C:
    peso_maximo = peso_B
    esfera_maxima = "B"
else:
    peso_maximo = peso_C
    esfera_maxima = "C"
# Va a mostrar en pantalla la respuesta de la esfera de mayor peso
print(f"La esfera de mayor peso es la esfera {esfera_maxima} con un peso de {peso_maximo} unidades.")
