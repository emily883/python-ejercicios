cadena=input("Introduce una cadena: ")


comprobador=cadena.upper()
conteo=0

for i in cadena:
    for o in comprobador:
        if o==i:
            conteo+=1



print(f"Tu cadena estupida tiene nada mas {conteo} letras mayusculas ")