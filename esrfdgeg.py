lista1=[1,2,3,5,6]
lista2=[7,8,3,9,4]

comprobacion=0



def superposicion(lista1,lista2):
	global comprobacion
	for i in lista1:
		for o in lista2:
			if i==o:
				comprobacion+=1
	if comprobacion!=0:
		print("True")
	else: 
		print("False")

	



superposicion(lista1,lista2)


