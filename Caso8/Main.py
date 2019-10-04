from Constants import *
from PIL import Image


def openImage(pPath):
    newImage = Image.open(pPath)
    return newImage


def createSectors():
    image = openImage(Images[0])
    imageWidth, imageHeight = image.size
    sectorsX = []
    sectorsY = []
    numberOfPixelsPerSectorX = imageWidth/numbersOfLines
    numberOfPixelsPerSectorY = imageHeight/numbersOfLines
    linePixelPositionX = 0
    linePixelPositionY = 0
    for actualNumberOfLines in range(0, numbersOfLines):
        linePixelPositionX += numberOfPixelsPerSectorX
        sectorsX += [linePixelPositionX]
        linePixelPositionY += numberOfPixelsPerSectorY
        sectorsY += [linePixelPositionY]

    print(sectorsX)
    print(sectorsY)


if __name__ == "__main__" :
    createSectors()