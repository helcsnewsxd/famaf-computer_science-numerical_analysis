from matplotlib import pyplot as plt

def graphic(x,y,l,t,b,n,f):
	fig,ax = plt.subplots()
	for i in range(0,len(x)):
		if not f[i]:
			ax.plot(x[i],y[i],'o',label=l[i])
		else:
			ax.plot(x[i],y[i],label=l[i])
	ax.set_xlabel("Eje X")
	ax.set_ylabel("Eje Y")
	ax.set_title(t)
	ax.grid()
	ax.legend()
	if(b==True):
		plt.show()
	else:
		plt.figure(n)
	return None
