def es_bisiesto(ano):
    if ano%4 == 0 and (not(ano%100 ==0)):
        print("El año es bisiestro :v ")
    elif ano%400 == 0:
        print("El año no es bisiestro")




ano=int(input("Indique el año: "))

es_bisiesto(ano)