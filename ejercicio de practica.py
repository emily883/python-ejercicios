from tkinter import *


root=Tk()

miframe=Frame(root, width=350, height=350)
miframe.pack()
palabra=StringVar()

def pantalla():
	palabra=entrada.get()
	palabra=palabra.lower()


	if palabra == "te amo" or palabra== "te quiero":
		sad=Label(miframe, text="Te quiero solo como amigo")
		sad.grid(row=3, column=1, columnspa=2, pady=10,padx=10)

	elif palabra == "te amo bebe":
		sadi=Label(miframe, text="Yo tambien Te amo mi amor")
		sadi.grid(row=4, column=1, columnspa=2, pady=10, padx=10)

	elif palabra == "nada":
		sada=Label(miframe, text="Gracias a Dios")
		sada.grid(row=5, column=1, columnspa=2 ,pady=10, padx=10)
	




label=Label(miframe, text="Que sientes por mi?", bg="red", fg="white").grid(row=0, column=1, columnspa=2, pady=10, padx=10)

entrada=Entry(miframe, fg="green", justify="center",textvariable=palabra)
entrada.grid(row=1, column=1, columnspa=2, pady=3, padx=3)


boton=Button(miframe, text="Enviar", bg="gray", command=lambda:pantalla())
boton.grid(row=2, column=1, columnspa=2, pady=5, padx=15)





root.mainloop()