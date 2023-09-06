# Ingresar el valor de la compra y el color de la bolita
VALCOMP = float(input("Ingrese el valor de la compra: "))
COLOR = input("Ingrese el color de la bolita (BLANCO, VERDE, AMARILLO, AZUL): ").upper() #el upper() sirve por si la persona ingresa el valor en minúscula cambie a mayúscula. 
# Inicializar el porcentaje de descuento
PDES = 0
# Calcular el porcentaje de descuento según el color de la bolita
if COLOR == "BLANCO":
    PDES = 0
elif COLOR == "VERDE":
    PDES = 10
elif COLOR == "AMARILLO":
    PDES = 25
elif COLOR == "AZUL":
    PDES = 50
else:
    PDES = 100
# Calcular el valor a pagar con el descuento aplicado
VALPAG = VALCOMP - (PDES * VALCOMP / 100)
# Mostrar el resultado
print(f"EL CLIENTE DEBE PAGAR: ${VALPAG}")
