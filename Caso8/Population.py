import math
import Constants
from Colors import Color
from PIL import Image, ImageDraw

listOfLines = []

class line:
    def __init__(self, pFirstCoordinate, pSecondCoordinate, pColor):
        self.__firstCoordinate = pFirstCoordinate
        self.__secondCoordinate = pSecondCoordinate
        self.__colorRange = getColorRange(pColor[0], pColor[1], pColor[2])

    def getFirstPoint(self):
        return self.__firstCoordinate

    def getSecondPoint(self):
        return self.__secondCoordinate

    def getColorRangeOfLines(self):
        return self.__colorRange

def getColorRange(pRed, pGreen, pBlue):
    if pRed <= 127 and pGreen <= 127 and pBlue <= 127:
        return 1
    elif pRed >= 128 and pGreen <= 127 and pBlue <= 127:
        return 2
    elif pRed <= 127 and pGreen >= 128 and pBlue <= 127:
        return 3
    elif pRed <= 127 and pGreen <= 127 and pBlue >= 128:
        return 4
    elif pRed >= 128 and pGreen >= 128 and pBlue <= 127:
        return 5
    elif pRed >= 128 and pGreen <= 127 and pBlue >= 128:
        return 6
    elif pRed >= 128 and pGreen >= 128 and pBlue >= 128:
        return 7
    else:
        return -1

def addImageLines(pImage):
    global listOfLines
    numberOfSectionsPerLine = Constants.IMAGESIZE[0] / Constants.NUMBER_OF_LINES + 1
    xPoint = Constants.IMAGESIZE[0] - 1
    newImage = Image.new("RGB", (Constants.IMAGESIZE[0], Constants.IMAGESIZE[1]))
    imageForDrawing = ImageDraw.Draw(newImage)
    imageForColor = ImageDraw.Draw(pImage)
    rgbImage = pImage.convert('RGB')
    sectorDivision = Constants.IMAGESIZE[0] // (Constants.NUMBER_OF_LINES + 1)

    for linesPerPixel in range(0, xPoint, 10):
        populationPerSector = []
        for moveRight in range(0, Constants.NUMBER_OF_LINES + 1):
            colorList = []
            linesList = []
            for pixelsPerLine in range(sectorDivision * moveRight, (sectorDivision * (moveRight + 1)) - 1):
                r, g, b = rgbImage.getpixel((pixelsPerLine, linesPerPixel))
                newColor = Color(r, g, b, pixelsPerLine, linesPerPixel)
                colorList += [newColor]
            r, g, b = doColorPromedy(colorList)
            imageForDrawing.line([(sectorDivision * moveRight, linesPerPixel), (sectorDivision * (moveRight + 1) - 1, linesPerPixel)], fill=(r, g, b), width=1)
            lines = line([sectorDivision * moveRight, linesPerPixel], [sectorDivision * (moveRight + 1) - 1, linesPerPixel], [r, g, b])
            listOfLines += [lines]
            linesList += [lines]

    print(len(listOfLines))
    uno = dos = tres = cuatro = cinco = seis = siete = 0
    for i in range(0, len(listOfLines)):
        revisar = listOfLines[i].getColorRangeOfLines()
        if revisar == 1:
            uno += 1
        elif revisar == 2:
            dos += 1
        elif revisar == 3:
            tres += 1
        elif revisar == 4:
            cuatro += 1
        elif revisar == 5:
            cinco += 1
        elif revisar == 6:
            seis += 1
        elif revisar == 7:
            siete += 1
    print(uno, dos, tres, cuatro, cinco, seis, siete)
    pImage.show()
    newImage.show()

def doColorPromedy(colorList):
    r = g = b = 0
    for colorPerList in (colorList):
        r += colorPerList.getRed()
        g += colorPerList.getGreen()
        b += colorPerList.getBlue()
    r = r // len(colorList)
    g = g // len(colorList)
    b = b // len(colorList)
    return r, g, b
