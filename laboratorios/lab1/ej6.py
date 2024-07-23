def comp(a,b):
	if a == b:
		return "IGUALES"
	elif a > b:
		return "PRIMERO"
	else:
		return "SEGUNDO"

print(comp(1,2))
print(comp(2,2))
print(comp(1.012301,1.01230))
