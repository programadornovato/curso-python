import random
contador=1
aleatorio=int(random.random()*100)
while True:
    numero=int(input(f"Humano que numero entre 1 y 100 crees que estoy pensando ({aleatorio}):"))
    if numero<aleatorio:
        print(f"Humano tonto el numero {numero} es menor al que estoy pensando")
    elif numero>aleatorio:
        print(f"Humano tonto el numero {numero} es mayor al que estoy pensando")
    if numero==aleatorio:
        print(f"FELICIDADES HUMANO LE ATINASTE AL NUMERO MAGICO EN {contador} INTENTOS")
        break
    contador=contador+1