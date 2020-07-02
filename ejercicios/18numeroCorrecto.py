divisor=float(input("Humano ingresa el divisor:"))
dividendo=float(input("Humano ingresa un dividendo superior a 0:"))
while dividendo<=0:
    print(f"Humano tonto el dividendo {dividendo} debe ser superior a 0 intentalo de nuevo:")
    dividendo=float(input())

divicion=divisor/dividendo
print(f"El resultado de la divicion es:{divicion}")