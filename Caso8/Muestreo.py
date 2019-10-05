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
    listaColoresSectores = []
    for sectores in range(0, 16):
        listaDeSector = []
        for colorXMuestra in range(0, 20):
            listaXSectores = []
            r, g, b = rgb_im.getpixel((lista[sectores][colorXMuestra][0], lista[sectores][colorXMuestra][1]))
            sumatoriaColores = r + g + b
            if(r != 0 and g != 0 and b != 0):
                listaXSectores = [[r*100 / sumatoriaColores, g*100 / sumatoriaColores, b*100 / sumatoriaColores]]
            elif(r != 0 and g != 0):
                listaXSectores = [[r*100 / sumatoriaColores, g*100 / sumatoriaColores, 0]]
            elif(g != 0 and b != 0):
                listaXSectores = [[0, g*100 / sumatoriaColores, b*100 / sumatoriaColores]]
            elif (r != 0 and b != 0):
                listaXSectores = [[r*100 / sumatoriaColores, 0, b*100 / sumatoriaColores]]
            else:
                listaXSectores = [[0, 0, 0]]
            listaDeSector += [listaXSectores]
        listaColoresSectores += [listaDeSector]
    print("Size listaColoresSectores: ", len(listaColoresSectores))
    prueba1 = 15
    prueba2 = 18
    rgb_im = image.convert('RGB')
    r, g, b = rgb_im.getpixel((lista[prueba1][prueba2][0], lista[prueba1][prueba2][1]))
    print("Sector: ", prueba1 + 1, " Muestra: ", prueba2 + 1, " Colores del Pixel -> Rojo: ", r, " Verde: ", g, " Azul: ", b)
    print("Porcentajes de cada color: ", listaColoresSectores[prueba1][prueba2])
    return listaColoresSectores