conteo= 0
letra=""
palabra=""
def  contarVocales():
    global conteo 
    global letra
    global palabra
    palabra=input("Indique una palabra: ").lower()
   

    letra=input("Indique una letra: ").lower()

    for i in palabra:
         if i == letra:
              conteo+=1



   




contarVocales()

print(f"Tu palabra tiene {conteo} de {letra} ")


