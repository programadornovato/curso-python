def pedirDatos():
    lista=[]
    while True:
        n=int(input("Humano ingres el numero que quieras (0 para terminar):"))
        if n==0:
            return lista
        else:
            lista.append(n)
    return lista

def burbuja(lista):
    tamano=len(lista)
    for _ in range(0,tamano):
        for j in range(0,tamano-1):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    return lista
def mostrarLista(lista):
    tam=len(lista)
    print("Humano aqui esta tu piche lista ordenada de forma acendente:")
    for i in range(0,tam):
        print(f"{lista[i]}")
    print("Humano aqui esta tu piche lista ordenada de forma desendente:")
    for i in range(tam,0,-1):
        print(f"{lista[i-1]}")

lista=pedirDatos()
lista=burbuja(lista)
mostrarLista(lista)