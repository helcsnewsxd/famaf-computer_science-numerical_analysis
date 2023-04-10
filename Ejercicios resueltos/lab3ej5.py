from graphic_function import graphic
import numpy as np
from scipy.interpolate import interp1d

datos = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos_aeroCBA.dat")

year = datos[:,0]
temp = datos[:,1]

year_interpol = year[~np.isnan(temp)]
temp_interpol = temp[~np.isnan(temp)]

interpol_type = ['linear','quadratic','cubic']
p = []
for it in interpol_type:
	p.append(interp1d(year_interpol,temp_interpol,kind=it,fill_value='extrapolate'))

year_plot = [year_interpol]
for i in range(0,3):
	year_plot.append(np.arange(1957,2018))
temps_plot = [temp_interpol]
for i in range(0,3):
	temps_plot.append(p[i](year_plot[i+1]))

graphic(year_plot,temps_plot,["data","linear","quadratic","cubic"],"Different types of interpolation with splines",True,0,[True]*4)
