'''
S o s: Suma.
R o r: Resta.
M o m: Multiplicación.
D o d: División.
'''
print("Humano ingresa dos numeros")
num1=int(input("Numero 1:"))
num2=int(input("Numero 2:"))
opcion=input("Humano selecciona lo que quieres hacer con eses dos numeros\n\
S s=Suma\n\
R r=Resta\n\
M m=Multiplicacion\n\
D d=Divicion\n"
)
opcion=opcion.lower()
res=0
if opcion=="s":
    res=num1+num2
if opcion=="r":
    res=num1-num2
if opcion=="m":
    res=num1*num2
if opcion=="d":
    if num2!=0:
        res=num1/num2
else:
    print("Humano estupido te di un menu y no le atinas ni al aire")
    quit()
print(f"Humano aqui esta tu ingao resultado:{res}")
    
