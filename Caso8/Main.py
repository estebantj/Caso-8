from Constants import *
from Muestreo import *
from PIL import Image, ImageDraw


def openImage(pPath):
    newImage = Image.open(pPath)
    return newImage


def createSectors():
    image = openImage(Images[0])
    imageWidth, imageHeight = image.size
    sectorsX = []
    sectorsY = []
    numberOfPixelsPerSectorX = imageWidth/(numbersOfLines+1)
    numberOfPixelsPerSectorY = imageHeight/(numbersOfLines+1)
    linePixelPositionX = 0
    linePixelPositionY = 0
    for actualNumberOfLines in range(0, numbersOfLines):
        linePixelPositionX += numberOfPixelsPerSectorX
        sectorsX += [linePixelPositionX]
        linePixelPositionY += numberOfPixelsPerSectorY
        sectorsY += [linePixelPositionY]

    imageForDrawing = ImageDraw.Draw(image)
    for coordinateNumber in range(0, numbersOfLines):
        x = sectorsX[coordinateNumber]
        y = sectorsY[coordinateNumber]
        imageForDrawing.line([(x, 0), (x, imageHeight)], fill="red", width=1)
        imageForDrawing.line([(0, y), (imageWidth, y)], fill="red", width=1)

    image.show()

    print(sectorsX)
    print(sectorsY)

if __name__ == "__main__" :
    image = openImage(Images[0])
    createSectors()
    listaMuestras = crearMuestreo()
    print("Lista de muestras del sector 1: ")
    print(listaMuestras[0])
    print("Lista de muestras del sector 5: ")
    print(listaMuestras[4])
    print("Lista de muestras del sector 9: ")
    print(listaMuestras[8])
    print("Lista de muestras del sector 13: ")
    print(listaMuestras[12])
    seleccionarMuestreo(image, listaMuestras)