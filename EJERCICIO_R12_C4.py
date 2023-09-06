# Ingresar  los datos del trabajador
NOM = input("Ingrese el nombre del trabajador: ")
NHT = int(input("Ingrese el número de horas trabajadas: "))
VHN = float(input("Ingrese el valor de la hora normal trabajada: "))
# Inicializar las variables
HET = 0  # Horas extras trabajadas
HEE8 = 0  # Horas extras que exceden de 8
SALARIO = 0  # Salario total
# Calcular horas extras si las horas trabajadas exceden de 40
if NHT > 40:
    HET = NHT - 40
    if HET > 8:
        HEE8 = HET - 8
        SALARIO = 40 * VHN + 16 * VHN + HEE8 * 3 * VHN
    else:
        SALARIO = 40 * VHN + HET * 2 * VHN
else:
    SALARIO = NHT * VHN
# Mostrar el resultado
print(f"EL TRABAJADOR {NOM} DEVENGO: ${SALARIO}")
