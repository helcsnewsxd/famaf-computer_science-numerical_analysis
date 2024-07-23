# Mis archivos
from graphic_function import graphic # Una función de otro .py que usé durante los labs por comodidad
from integracion import trapecio_adaptativo # Inciso B

def recupera_dato():
    x = [0,1.5,2,2.9,4,5.6,6,7.1,8.05,9.2,10,11.3,12]
    y = [0.1,0.2,1,0.56,1.5,2.0,2.3,1.3,0.8,0.6,0.4,0.3,0.2]
    return x,y

def incisoA(x,y):
    graphic([x],[y],["Datos de medición"],"Terreno a remover",True,1,[False])

def incisoC(x,y):
    print(f"Deben ser removidos, aproximadamente, {trapecio_adaptativo(x,y)*10} metros cúbicos de tierra para nivelar a 0 el terreno considerado\n")

# Main
def ejercicio2():
    x,y = recupera_dato()
    incisoA(x,y)
    incisoC(x,y)