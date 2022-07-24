from scipy.interpolate import interp1d

def test():
	x = [123,342,324,45]
	y = [1,2,3,4]
	z = [5,6,7]
	p = interp1d(x,y,kind = 'cubic',fill_value = 'extrapolate')
	print(p(z))
	
test()
