x=0
y=1
z=0
while True:
    n=int(input("Humano por favor ingresa un numero mayor a 1:"))
    if n>1:
        break
print("1",end=" ")
for i in range(0,n):
    z=x+y
    print(f"{z}",end=" ")
    x=y
    y=z
print("")