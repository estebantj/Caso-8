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
    linesList = []
    xPoint = Constants.IMAGESIZE[0] - 1
    newImage = Image.new("RGB", (Constants.IMAGESIZE[0], Constants.IMAGESIZE[1]))
    imageForDrawing = ImageDraw.Draw(newImage)
    imageForColor = ImageDraw.Draw(pImage)
    rgbImage = pImage.convert('RGB')
    sectorDivision = Constants.IMAGESIZE[0] // (Constants.NUMBER_OF_LINES + 1)
    red = yellow = black = orange = blue = gray = 0
    for linesPerPixel in range(0, xPoint):
        for moveRight in range(0, Constants.NUMBER_OF_LINES + 1):
            colorList = []
            for pixelsPerLine in range(sectorDivision * moveRight, sectorDivision * (moveRight + 1)):
                r, g, b = rgbImage.getpixel((pixelsPerLine, linesPerPixel))
                newColor = Color(r, g, b, pixelsPerLine, linesPerPixel)
                colorList += [newColor]
            r, g, b = doColorPromedy(colorList)
            imageForDrawing.line(
                [(sectorDivision * moveRight, linesPerPixel), (sectorDivision * (moveRight + 1), linesPerPixel)],
                fill=(r, g, b), width=1)
            linesList += [colorList]
            listOfLines += [
                line([sectorDivision * moveRight, linesPerPixel], [sectorDivision * (moveRight + 1), linesPerPixel],
                     [r, g, b])]
    # originalImage.show()
    # newImage.show()


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
