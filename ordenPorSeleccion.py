def insertarNumero():
    lista=[]
    while True:
        n=int(input("Humano por favor ingresa un numero (0 terminar):"))
        if n==0:
            return lista
        else:
            lista.append(n)
def ordenPorSeleccion(lista):
    tamaño=len(lista)
    for i in range(0,tamaño):
        min=i
        for j in range(i+1,tamaño):
            if lista[min]>lista[j]:
                min=j
        aux=lista[i]
        lista[i]=lista[min]
        lista[min]=aux
    return lista
def mostrarLista(lista):
    for numero in lista:
        print(numero)

lista=insertarNumero()
ordenPorSeleccion(lista)
print("Humano aqui estan tus pinches numeros ordenados:")
mostrarLista(lista)