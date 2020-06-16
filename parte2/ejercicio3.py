palabra1=input("Indique una palabra: ")
palabra2=input("Indique otra palabra: ")
numero=int(input("Indique el numero: "))

print("Se te devolvera la palabra que tiene mas caracteres que el numero q introduciste")

def filtrarPalabras():
    global palabra1,palabra2,numero

    pala1=len(palabra1)
    pala2=len(palabra2)
    
    if pala1>numero:
        print(palabra1)
    elif pala2>numero:
        print(palabra2)
    else:
        print("Las dos palabras tienen la misma cantidad de letras")
    



filtrarPalabras()