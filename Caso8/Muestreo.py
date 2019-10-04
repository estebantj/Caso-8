import random
def crearMuestreo():
    muestreoDeSectores = []
    puntoX1 = 0
    puntoY1 = 256
    puntoX2 = 0
    puntoY2 = 256
    divisionSectores = 256
    for desplazamientoHorizontal in range(2, 6):
        for desplazamientoVertical in range(2, 6):
            sectores = []
            for creacionDeMuestras in range(0, 20):
                sectores += [[random.randint(puntoX1, puntoY1), random.randint(puntoX2, puntoY2)]]
            muestreoDeSectores += [sectores]
            puntoX1 = puntoY1
            puntoY1 = divisionSectores * desplazamientoVertical
        puntoX2 = divisionSectores * (desplazamientoHorizontal - 1)
        puntoY2 = divisionSectores * desplazamientoHorizontal
        puntoX1 = 0
        puntoY1 = 256
    return muestreoDeSectores