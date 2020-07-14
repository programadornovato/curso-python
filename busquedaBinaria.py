import modulos.humano as humus
import modulos.busquedas as busquedas
lista=[1,2,3,4,5,6,7,8,9,10]
while True:
    num=humus.pedirNumero(lista)
    encontrado=busquedas.busquedaBinaria(lista,num)
    if encontrado==True:
        print("Felicidades humano el numero ingresado esta en la lista ahora dame la patita :)")
        break
    else:
        print("Humano tonto el numero no esta en la lista intentalo de nuevo:")
