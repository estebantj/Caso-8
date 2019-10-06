import random
from Colors import Color
import Constants
from Sector import Sector

def crearMuestreo():
    muestreoDeSectores = []
    puntoX1 = puntoY1 = 0
    puntoX2 = puntoY2 = 0
    divisionSectores = 256
    sectorNumber = 1
    for desplazamientoHorizontal in range(1, 5):
        puntoX2 = puntoY2
        puntoY2 = divisionSectores * desplazamientoHorizontal

        for desplazamientoVertical in range(1, 5):
            sectores = []
            puntoX1 = puntoY1
            puntoY1 = divisionSectores * desplazamientoVertical

            for creacionDeMuestras in range(0, Constants.NUMBERS_OF_SAMPLES_PER_SECTOR):
                xCoordinate = random.randint(puntoX1, puntoY1)
                yCoordinate = random.randint(puntoX2, puntoY2)
                if xCoordinate == Constants.IMAGESIZE[0]:
                    xCoordinate -= 1
                if yCoordinate == Constants.IMAGESIZE[1]:
                    yCoordinate -= 1
                sectores += [[xCoordinate, yCoordinate]]
            newSector = Sector(sectores)
            newSector.setSectorNumber(sectorNumber)
            muestreoDeSectores += [newSector]
            sectorNumber += 1
        puntoX1 = 0
        puntoY1 = 0
    return muestreoDeSectores



def seleccionarMuestreo(image, lista):
    rgb_im = image.convert('RGB')
    listaColoresSectores = []
    for eachSector in lista:
        listaDeSector = []
        sumatoriaColores = [0, 0, 0]
        for eachCoordinateSample in eachSector.getCoordinateSamples():
            r, g, b = 0, 0, 0
            try:
                r, g, b = rgb_im.getpixel((eachCoordinateSample[0], eachCoordinateSample[1]))
            except IndexError:
                print("BIG ASS ERROR")
                print((eachCoordinateSample[0], eachCoordinateSample[1]))
            colorDeMuestra = Color(r, g, b)
            sumatoriaColores[0] += r
            sumatoriaColores[1] += g
            sumatoriaColores[2] += b
            listaDeSector += [colorDeMuestra]
        eachSector.setColorSamples(listaDeSector)
        # Aca se saca el promedio
        # Se divide la sumatoria de los colores entre la cantidad de muestras, que es 20
        promedios = [sumatoriaColores[0] / 20, sumatoriaColores[1] / 20, sumatoriaColores[2] / 20]
        print("Promedios del sector", promedios)
        listaColoresSectores += [listaDeSector]


def estimateWhiteColor(samplesPerSector):
    whitePercentajePerSectorList = []
    sectorNumber = 1
    for listOfSamples in samplesPerSector:
        whiteSamples = 0
        nonWhiteSamples = 0
        for eachColor in listOfSamples:
            if eachColor.isWhite():
                whiteSamples += 1
            else:
                nonWhiteSamples += 1
        whitePercentaje = (whiteSamples * 100) / Constants.NUMBERS_OF_SAMPLES_PER_SECTOR
        print("Sector white percentaje: ", whitePercentaje)
        sectorNumber += 1
    return whitePercentajePerSectorList
