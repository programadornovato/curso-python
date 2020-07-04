'''
Programa que pida numero enteros y los vaya sumando.
Si el número introducido esta dentro de 100 y 200 o es 0 cerrar el programa.
'''
suma=0
while True:
    numero=int(input("Humano ingresa un numero entre 100 y 200 para ser sumado si precionas 0 se cierra el programa:"))
    if numero>=100 and numero<=200:
        suma=suma+numero
        print(f"Humano aqui esta tu pinche suma: {suma}")
    else:
        print(f"Humano tonto solo se pueden sumar numeros entre 100 y 200 aqui esta tu suma {suma}")
    if numero==0:
        break