conteo=9
mayor=0
edades=[]

while conteo!=0:
    edad=int(input("Indique la edad: "))
    edades.append(edad)
    conteo-=1

lista=tuple(edades)

for i in lista:
    if i > 20:
        mayor+=1

print(f"Hay {mayor} personas mayores de 20 años")











