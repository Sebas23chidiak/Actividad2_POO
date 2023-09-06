# Ingresar el nombre del empleado
nombre = input("Ingrese el nombre del empleado: ")
# Ingresar el salario básico por hora y el número de horas trabajadas en el mes
salario_por_hora = float(input("Ingrese el salario básico por hora: "))
horas_trabajadas = int(input("Ingrese el número de horas trabajadas en el mes: "))
# Calcular el salario mensual
salario_mensual = salario_por_hora * horas_trabajadas
# Comprobar si el salario mensual es mayor de $450,000
if salario_mensual > 450000:
    print(f"Nombre del empleado: {nombre}")
    print(f"Salario mensual: ${salario_mensual:.2f}")
else:
    print(f"Nombre del empleado: {nombre}")
