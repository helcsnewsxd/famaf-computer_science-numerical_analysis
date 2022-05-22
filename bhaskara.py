from math import sqrt

def bhaskara(p):
	a,b,c=p[0],p[1],p[2]

	disc=b**2-4*a*c

	if(disc<0):
		return [None,None],True

	if(b>0):
		x1=(-b-sqrt(disc))/(2.0*a)
	else:
		x1=(-b+sqrt(disc))/(2.0*a)

	x2=(c/a)/x1
	return [x1,x2],False
