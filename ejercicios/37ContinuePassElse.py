'''
Crear un programa en python que pida al humano que ingrese una sucesión de números pares ascendentes (de menor a mayor).
Pedir al humano un número par:
    Si es par guardarlo en una lista de lo contrario no.
Validar que los números que ingresó sean ascendentes y mostrarle al humano el resultado:
'''
lista=[]
while True:
    num=int(input("humano por favor ingresa un numero par (0 para terminar):"))
    if num%2==0:
        pass
    else:
        continue
    if num==0:
        break
    lista.append(num)

print(lista)

i=0
while i<len(lista):
    if i>0:
        if lista[i]<= lista[i-1]:
            esAcendente=False
            break
    i=i+1
else:
    esAcendente=True
print("Es acendente:",esAcendente)

