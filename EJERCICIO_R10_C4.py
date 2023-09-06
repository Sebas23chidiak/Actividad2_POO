# ingresar los datos del estudiante
NI = input("Ingrese el número de inscripción: ")
NOM = input("Ingrese el nombre del estudiante: ")
PAT = float(input("Ingrese el patrimonio del estudiante: "))
ES = int(input("Ingrese el estrato social del estudiante: "))
# Pago de matrícula inicial
PAGMAT = 50000
# Comprobar las condiciones para aplicar un aumento en el pago de matrícula
if PAT > 2000000 and ES > 3:
    aumento = 0.03 * PAT
    PAGMAT += aumento
# Mostrar el resultado
print(f"EL ESTUDIANTE CON NUMERO DE INSCRIPCION {NI} Y NOMBRE {NOM} DEBE PAGAR: ${PAGMAT}")
