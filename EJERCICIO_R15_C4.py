# Solicitar los pesos de las esferas A, B, C y D
PESOA = int(input("Ingrese el peso de la esfera A: "))
PESOB = int(input("Ingrese el peso de la esfera B: "))
PESOC = int(input("Ingrese el peso de la esfera C: "))
PESOD = int(input("Ingrese el peso de la esfera D: "))

# Comprobar cuál es la esfera diferente y si es mayor o menor peso
if (PESOA == PESOB) and (PESOA == PESOC):
    if PESOD > PESOA:
        print("LA ESFERA D ES LA DIFERENTE Y ES DE MAYOR PESO")
    else:
        print("LA ESFERA D ES LA DIFERENTE Y ES DE MENOR PESO")
elif (PESOA == PESOB) and (PESOA == PESOD):
    print("LA ESFERA C ES LA DIFERENTE")
    if PESOC > PESOA:
        print("Y ES DE MAYOR PESO")
    else:
        print("Y ES DE MENOR PESO")
elif (PESOA == PESOC) and (PESOA == PESOD):
    print("LA ESFERA B ES LA DIFERENTE")
    if PESOB > PESOD:
        print("Y ES DE MAYOR PESO")
    else:
        print("Y ES DE MENOR PESO")
else:
    print("LA ESFERA A ES LA DIFERENTE")
    if PESOA > PESOB:
        print("Y ES DE MAYOR PESO")
    else:
        print("Y ES DE MENOR PESO")
