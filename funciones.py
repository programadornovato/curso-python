def suma(n1,n2):
    res=n1+n2
    return float(res)
def resta(n1,n2):
    res=n1-n2
    return str(res)

#print("Hola desde la funcion print soy un parametro")
num1=10
num2=5
while True:
    print(f"Humano selecciona que deseas hacer con estos numero {num1} y {num2}:\n\
1.-Sumar\n\
2.-Restar\n\
3.-Salir")
    opcion=input()
    if opcion=='1':
        res=suma(num1,num2)
        res=res+1
        print(f"El resultado es:{res} tipo:{type(res)}")
    elif opcion=='2':
        res=resta(num1,num2)
        res=res+1
        print(f"El resultado es:{res} tipo:{type(res)}")
    elif opcion=='3':
        break
    else:
        print("humano tonto elije un numero de las opciones")
