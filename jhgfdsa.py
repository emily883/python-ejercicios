caracter=(input("Digite el caracter q quieres q se multiplique: "))
num2=int(input("Digite el numero multiplicador: "))

otro=0
def generar(caracter,num2):
	 global otro

	 while otro!=num2:
	 	print(caracter)
	 	otro+=1



generar(caracter,num2)



'''def generar(caracter,num2):
	print(caracter * num2)'''