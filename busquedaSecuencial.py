def pedirNumero(lista):
    for numero in lista:
        print(numero,end=" ")
    num=int(input("\nHumano por favor ingresa un numero de la lista anterior:"))
    return num
def busquedaSecuencia(lista,num):
    for i in range(0,len(lista)):
        if num==lista[i]:
            return True
    return False
lista=[1,2,3,4,5]
while True:
    num=pedirNumero(lista)
    encontrado=busquedaSecuencia(lista,num)
    if encontrado==True:
        print("Felicidades humano haz colocado un numero de la lista ahora dame la patita:)")
        break
    else:
        print("Humano tonto intentalo de nuevo:")