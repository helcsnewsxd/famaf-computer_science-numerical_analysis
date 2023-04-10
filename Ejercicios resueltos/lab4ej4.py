from graphic_function import graphic
import numpy as np

def input():
	data = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/covid_italia.csv',delimiter=',',usecols=1)
	return data

y = input()
x = np.arange(0,len(y)) # porque son len(x) días seguidos

# y = a * e**(bx)
# ln y = ln a + bx
	# Luego,
		# na = ln a
		# ny = ln y
	# de modo que
		# ny = na + b * x

ny = np.log(y)
p = np.polyfit(x,ny,1)
b,a = p[0],np.exp(p[1])

graphic([x]*2,[y,a * np.exp(b*x)],["Casos de Covid diarios","Ajuste exponencial"],"Ajuste exponencial de la cantidad de infectados en Italia bajo el modelo y = ae^(bx)",True,1,[False,True])
