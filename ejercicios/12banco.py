total=1000
print("¡¡¡Bienvenido pequeño mortal al banco!!!\n\
Que quieres hacer\n\
1.- Ingresar dinero:\n\
2.- Sacar dinero:\n\
3.-Salir:\n")
opcion=int(input())
if opcion==1:
    ingreso=float(input("¿Cuanto dinero deseas ingresar?:"))
    total+=ingreso
    print(f"Tu saldo es de {total:.2f}")
elif opcion==2:
    egreso=float(input("¿Cuanto dinero deseas sacar?:"))
    if total-egreso<0:
        print(f"Pinche humano cabron, no tuenes tanto diner, tu saldo solo es de {total:.2f}")
    else:
        total-=egreso
        print(f"Tu saldo es de {total:.2f}")
elif opcion==3:
    quit()
