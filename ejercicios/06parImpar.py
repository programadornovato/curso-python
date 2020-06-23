numero1=int(input("Humano inresa un numero par:"))
numero2=int(input("Humano inresa otro numero par:"))
numeroPar1=numero1%2
numeroPar2=numero2%2
if numeroPar1==0 and numeroPar2==0:
    print("Buen chico, ahora dame la patita")
else:
    print("Humano tonto, los dos numeros deberian ser par")
    if numeroPar1!=0:
        print(f"El numero {numero1} no es par")
    if numeroPar2!=0:
        print(f"El numero {numero2} no es par")