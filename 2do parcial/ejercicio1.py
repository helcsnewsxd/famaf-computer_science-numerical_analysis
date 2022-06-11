from numpy import loadtxt

# Mis archivos
from graphic_function import graphic # Una función de otro .py que usé durante los labs por comodidad
from interpolacion import * # Están Lagrange y Spline Cúbico

# Separo la información del documento y la acomodo en los datos a usar para el problema
def recupera_dato():
    data = loadtxt(fname='irma.csv',dtype=float,delimiter=',')
    return data[:,0],data[:,1],data[:,2]

def incisoA(longitud,latitud):
    graphic([longitud],[latitud],["Datos de posición"],"Coordenadas del huracán Irma - Florida 10/09/2017",False,1,[False])

def incisoB(hora,longitud,latitud):
    x_hora = range(0,25)
    lagrange = [ilagrange(hora,longitud,x_hora), ilagrange(hora,latitud,x_hora)]
    spline = [spline_cubico(hora,longitud,x_hora), spline_cubico(hora,latitud,x_hora)]

    # Los datos para graficar entonces son:
    x = [longitud,lagrange[0],spline[0]]
    y = [latitud,lagrange[1],spline[1]]
    graphic(x,y,["Datos de posición","Lagrange","Spline cúbico"],"Coordenadas del huracán Irma - Florida 10/09/2017 (interpolación de los datos)",True,2,[False,True,True])

# Main
def ejercicio1():
    hora, longitud, latitud = recupera_dato()
    incisoA(longitud,latitud)
    incisoB(hora,longitud,latitud)
