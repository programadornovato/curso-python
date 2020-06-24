'''
Entre 0 y 1 años es junior
Entre 1 y 3 años es semi senior
Entre 3 y 5 años es senior
Más de 5 años es un Dios
'''
anios=int(input("Cuantoas años de experiencia tienes: "))
if 0 <= anios<1:
    print("El humao es cadidato para ser junior")
elif 1 <= anios<3:
    print("El humao es cadidato para ser semi senior")
elif 3 <= anios<5:
    print("El humao es cadidato para ser senior")
elif anios >=5:
    print("El humao es cadidato para ser Dios")