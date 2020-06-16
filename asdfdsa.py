palabra=input("Introduce una palabra y te dire si es palindromo o no :v : ")

invertida=palabra[::-1]



def palindromo(palabra, invertida):
	
	if palabra==invertida:
		print("Si es palindroma su palabra :v")
	else:
		print("No lo es :v ")




palindromo(palabra,invertida)