ano=int(input("Ingrese el año en curso: "))

nombre1=input("ingrese el nombre de la persona 1:  ")
nombre2=input("ingrese el nombre de la persona 2:  ")
nombre3=input("ingrese el nombre de la persona 3:  ")

ano1=int(input("Indique el año de nacimiento de la persona 1: "))
ano2=int(input("Indique el año de nacimiento de la persona 2: "))
ano3=int(input("Indique el año de nacimiento de la persona 3: "))

persona1=[]
persona2=[]
persona3=[]

persona1.append(nombre1)
persona2.append(nombre2)
persona3.append(nombre3)

persona1.append(ano1)
persona2.append(ano2)
persona3.append(ano3)

edad1=0
edad2=0
edad3=0


while ano1!=ano:
    edad1+=1
    ano1+=1

print(f"La persona 1 cumplira {edad1} años mientras este cursando el año")


while ano2!=ano:
    edad2+=1
    ano2+=1

print(f"La persona 2 cumplira {edad2} años mientras este cursando el año")


while ano3!=ano:
    edad3+=1
    ano3+=1

print(f"La persona 3 cumplira {edad3} años mientras este cursando el año")
