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

    lista = crearMuestreo()
    print(lista[0][0])
    print(lista[4])
    print(lista[9])
    print(lista[15])

    rgb_im = image.convert('RGB')
    r, g, b = rgb_im.getpixel((lista[5][16][0], lista[5][16][1]))
    print("Cantidad de color en el Pixel -> Rojo: ", r, " Verde: ", g, " Azul: ", b)

if __name__ == "__main__" :
    createSectors()