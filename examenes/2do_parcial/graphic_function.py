from matplotlib import pyplot as plt

# Breve explicación de la función graphic:
	# Es una función hecha durante el semestre para facilitar y agilizar la realización de los laboratorios propuestos

	# x[i], y[i], func_labels[i] representan los puntos (x,y) y el nombre de la i-ésima función a graficar
	# func_title es el título del gráfico
	# hago_muestra es un booleano que sirve para saber si necesito hacer varias figuras o solo una (hago_muestra == False sirve para ir juntando los gráficos y cuando se ponga haga_muestra == True, salten todos juntos)
	# figure_number representa el nro de figura a poner (en el caso que hago_muestra == False)
	# dibujo_funcion es un array de booleanos que, básicamente, si dibujo_funcion[i] es True, entonces dibujo los (x[i][j],y[i][j]) uniéndolos mediante rectas
		# En caso contrario, si dibujo_funcion[i] == False, los (x[i][j],y[i][j]) se dibujan como puntos independientes

def graphic(x,y,func_labels,func_title,hago_muestra,figure_number,dibujo_funcion):
	fig,ax = plt.subplots()
	for i in range(0,len(x)):
		if not dibujo_funcion[i]:
			ax.plot(x[i],y[i],'o',label=func_labels[i])
		else:
			ax.plot(x[i],y[i],label=func_labels[i])
	ax.set_xlabel("Eje X")
	ax.set_ylabel("Eje Y")
	ax.set_title(func_title)
	ax.grid()
	ax.legend()
	if(hago_muestra==True):
		plt.show()
	else:
		plt.figure(figure_number)
	return None
