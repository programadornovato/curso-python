def pedirNumero(lista):
    for numero in lista:
        print(numero,end=" ")
    num=int(input("\nHumano por favor ingresa un numero de la lista anterior:"))
    return num
def busquedaBinaria(lista,num):
    tam=len(lista)
    cont=0
    inf=0
    sup=tam
    while inf<=sup and cont<tam:
        mitad=int((inf+sup)/2)
        if lista[mitad]==num:
            return True
        elif lista[mitad]>num:
            sup=mitad
            mitad=int((inf+sup)/2)
        elif lista[mitad]<num:
            inf=mitad
            mitad=int((inf+sup)/2)
        cont=cont+1
    return False
lista=[1,2,3,4,5,6,7,8,9,10]
while True:
    num=pedirNumero(lista)
    encontrado=busquedaBinaria(lista,num)
    if encontrado==True:
        print("Felicidades humano el numero ingresado esta en la lista ahora dame la patita :)")
        break
    else:
        print("Humano tonto el numero no esta en la lista intentalo de nuevo:")
