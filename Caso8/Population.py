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
    elif pRed <= 127 and pGreen >= 128 and pBlue >= 128:
        return 6
    elif pRed >= 128 and pGreen <= 127 and pBlue >= 128:
        return 7
    elif pRed >= 128 and pGreen >= 128 and pBlue >= 128:
        return 8
    else:
        return -1


def createPopulationPerSector(pSectorList, pImage):
    global listOfLines
    rgbImage = pImage.convert('RGB')
    for sector in pSectorList:
        amountOfLinesCreated = 0
        for amountOfLines in range(sector.getYRange()[0], sector.getYRange()[1], 2):
            colorList = []
            for pixelsPerLine in range(sector.getXRange()[0], sector.getXRange()[1]):
                r, g, b = rgbImage.getpixel((pixelsPerLine, amountOfLines))
                newColor = Color(r, g, b, pixelsPerLine, amountOfLines)
                colorList += [newColor]
            r, g, b = doColorPromedy(colorList)
            lines = line([sector.getXRange()[0], amountOfLines],
                         [sector.getXRange()[1], amountOfLines], [r, g, b])
            listOfLines += [lines]
            sector.addIndividualToPopulation(lines)
            amountOfLinesCreated += 1


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
    #pImage.show()
    #newImage.show()


def countPopulation(pPopulation):
    firstRange = secondRange = thirdRange = fourthRange = fifthRange = sixRange = seventhRange = eighth = 0
    for i in range(0, len(listOfLines)):
        revisar = pPopulation[i].getColorRangeOfLines()
        if revisar == 1:
            firstRange += 1
        elif revisar == 2:
            secondRange += 1
        elif revisar == 3:
            thirdRange += 1
        elif revisar == 4:
            fourthRange += 1
        elif revisar == 5:
            fifthRange += 1
        elif revisar == 6:
            sixRange += 1
        elif revisar == 7:
            seventhRange += 1
        elif revisar == 8:
            eighth += 1
    return firstRange, secondRange, thirdRange, fourthRange, fifthRange, sixRange, seventhRange, eighth


def createChromosomeRepresentation():
    global listOfLines
    populationPerRange = countPopulation(listOfLines)
    totalPopulation = sum(populationPerRange)
    print()
    pass


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
