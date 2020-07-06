while True:
    n=int(input("Humano por favor ingresa un numero mayor a 1:"))
    if n>1:
        break
    else:
        print("Humano tonto te pedi un numero mayor a 1")
suma=0
strResultado=""
for i in range(1,n+1):
    suma=suma+i
    #print(f"{i}",end="+")
    strResultado=strResultado+str(i)+"+"
strResultado=strResultado[:-1]
strResultado=strResultado+"="
print(strResultado)
print(f"Aqui esta tu pinche suma:{suma}")