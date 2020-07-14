import modulos.humano as humus
import modulos.busquedas as busquedas
lista=[1,2,3,4,5]
while True:
    num=humus.pedirNumero(lista)
    encontrado=busquedas.busquedaSecuencia(lista,num)
    if encontrado==True:
        print("Felicidades humano haz colocado un numero de la lista ahora dame la patita:)")
        break
    else:
        print("Humano tonto intentalo de nuevo:")