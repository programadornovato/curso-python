while True:
    n=int(input("Huamno POR FAVOR ingresa un numero mayor a 1:"))
    if n>1:
        break
    else:
        print("Humano te pedi POR FAVOR que ingresara un numero mayor a 1 intentalo de nuevo")
factorial=1
strResultado=""
for i in range(1,n+1):
    factorial=factorial*i
    strResultado=strResultado+str(i)+"*"
strResultado=strResultado[:-1]
strResultado=strResultado+"="
print(strResultado)
print(f"Humano aqui esta tu piche factorial:{factorial}")