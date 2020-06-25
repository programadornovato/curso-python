'''
Primer elemento
Último elemento
Un elemento que no está en la lista.
Rango del primero al tercero.
Rango del tercero al último.
'''
lista=[
    "Hola",
    "humano",
    "como",
    "estas",
    1,
    2,
    3.33,
    [
        4,5,6
    ]
]
print(lista)
print("Primer elemento:",lista[0])
print("Último elemento:",lista[-1])
#print("Un elemento que no está en la lista:",lista[9])
print("Rango del primero al tercero:",lista[:3])
print("Rango del tercero al último:",lista[3:])
