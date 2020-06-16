palabra1 =input("Indique una palabra: ")
palabra2=input("Indique otra palabra y te dire cual es mas larga xd: ")





def funcionMasLarga():
    global palabra1
    global palabra2

    indice1=len(palabra1)
    indice2=len(palabra2)

    if indice1>indice2:
        print(f"La palabra {palabra1} es mas larga :v ")
    elif indice2>indice1:
        print(f"La palabra {palabra2} es mas larga :v xd")
    else:
        print("Las dos palabras son iguales")




funcionMasLarga()
