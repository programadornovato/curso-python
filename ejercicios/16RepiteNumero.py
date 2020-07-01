'''
En este ejercicio le mostraremos una lista de números al humano y pediremos que ingrese un número y la cantidad de veces que ese número se repite.

Crearemos una tupla con números al azar y  se la mostraremos al humano.
Pediremos al humano que ingrese un numero de la tupla y nos diga cuantas veces se repite.
Si le atina felicitamos al humano.
En caso contrario reprendemos al humano.

'''
tupla=(1,2,4,2,5,6,7,8,15,2,3)
print(tupla)
numero=int(input("Humano ingresa un numero de la lista:"))
if numero in tupla:
    print(f"Humano cuantas veces se repite el numero {numero} en la lista:")
    repite=int(input())
    seRepiteEnTupla=tupla.count(numero)
    if repite==seRepiteEnTupla:
        print("Buen chico ahora dame la patita :)")
    else:
        print(f"Humano tonto el numero {numero} se repite {seRepiteEnTupla} en la lista")
else:
    print(f"Humano tonto el numero {numero} no esta en la lista")