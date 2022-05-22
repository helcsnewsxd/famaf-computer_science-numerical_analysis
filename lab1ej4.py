x = 0
while x != 10:
	x = x+0.1
	
#El programa queda colgado, nunca termina ya que el ciclo
#es infinito porque nunca se va a llegar exactamente a 10
#por el error de representacion

#Esto se debe a que 0.1 en nro binario tiene una representacion binaria fraccionaria periodica, por lo que el redondeo o truncamiento genera si o si un error

#Sumando 0.5 no se produce inconveniente ya que su representacion binaria es finita
