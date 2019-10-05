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

def seleccionarMuestreo(image, lista):
    rgb_im = image.convert('RGB')
    listaColoresSector = []
    for sectores in range(0, 15):
        listaXSector = []
        for colorXSector in range(0, 20):
            listaXColor = []
            r, g, b = rgb_im.getpixel((lista[sectores][colorXSector][0], lista[sectores][colorXSector][1]))
            sumatoriaColores = r + g + b
            if(r != 0 and g != 0 and b != 0):
                listaXColor = [[r*100 // sumatoriaColores, g*100 // sumatoriaColores, b*100 // sumatoriaColores]]
            elif(r != 0 and g != 0):
                listaXColor = [[r*100 // sumatoriaColores, g*100 // sumatoriaColores, 0]]
            elif(g != 0 and b != 0):
                listaXColor = [[0, g*100 // sumatoriaColores, b*100 // sumatoriaColores]]
            elif (r != 0 and b != 0):
                listaXColor = [[r*100 // sumatoriaColores, 0, b*100 // sumatoriaColores]]
            else:
                listaXColor = [[0, 0, 0]]
            listaXSector += [listaXColor]
            ##print("Sector: ", sectores+1, " Colores del Pixel -> Rojo: ", r, " Verde: ", g, " Azul: ", b)
        listaColoresSector += [listaXSector]
    rgb_im = image.convert('RGB')
    r, g, b = rgb_im.getpixel((lista[13][0][0], lista[13][0][1]))
    print("Sector: ", 14, " Colores del Pixel -> Rojo: ", r, " Verde: ", g, " Azul: ", b)
    print(listaColoresSector[0])