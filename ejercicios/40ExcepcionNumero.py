def leerNumero():
    while True:
        valor=input("Humano ingres un numero que sea un numero:")
        try:
            numero=int(valor)
            return numero
        except ValueError as ex:
            print(f"Humano tonto el valor '{valor}' no es numero intentalo de nuevo ",ex)
lista=[]
print("Ingresa una lista de numeros (0 para terminar)")
while True:
    numero=leerNumero()
    if numero==0:
        break
    else:
        lista.append(numero)

print("Humano ingresa un indice de tu lista: ",lista)
try:
    print(f"Este es el numero de tu indice ",lista[leerNumero()])
except IndexError as ex:
    print("El indice no esta en la lista ",ex)
