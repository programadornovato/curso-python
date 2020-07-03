'''
for i in range(5):
    print("Numero:",i)

for i in [5,6,7]:
    print("Numero:",i)

for i in (5,6,7):
    print("Numero:",i)

diccionario={"Python":1,"Java":2,"JavaScript":3}
for lenguaje in diccionario:
    print(f"{lenguaje} -> {diccionario[lenguaje]} ")

for clave,valor in {"Python":1,"Java":2,"JavaScript":3}.items():
    print(f"{clave} -> {valor}")
'''
texto="programadornovato"
for letra in texto:
    print("Dame una:",letra)
print("Como dice:",texto)
