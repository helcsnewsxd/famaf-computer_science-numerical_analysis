from matplotlib import pyplot as plt

def graphic(x,y,func_lables,func_title,hago_muestra,figure_number,dibujo_funcion):
	fig,ax = plt.subplots()
	for i in range(0,len(x)):
		if not dibujo_funcion[i]:
			ax.plot(x[i],y[i],'o',label=func_lables[i])
		else:
			ax.plot(x[i],y[i],label=func_lables[i])
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
