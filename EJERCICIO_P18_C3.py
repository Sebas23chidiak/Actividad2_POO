# se le pide al usuario que ingrese la información del empleado
codigo_empleado = input("Ingrese el código del empleado: ")
nombres = input("Ingrese el nombre del empleado: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas al mes: "))
valor_hora = float(input("Ingrese el valor de la hora trabajada: "))
porcentaje_retencion = float(input("Ingrese el porcentaje de retención en la fuente (%): "))

# Calcular el salario bruto
salario_bruto = horas_trabajadas * valor_hora

# Calcular la retención en la fuente
retencion = (porcentaje_retencion / 100) * salario_bruto

# Calcular el salario neto
salario_neto = salario_bruto - retencion

# Mostrar la información del empleado, muestra la información del empleador, código, nombres, salario bruto y salario neto
print("\nInformación del empleado:")
print("Código del empleado:", codigo_empleado)
print("Nombres:", nombres)
print("Salario Bruto:", salario_bruto)
print("Salario Neto:", salario_neto)
