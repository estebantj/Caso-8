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


def countPopulation(pPopulation):
    firstRange = secondRange = thirdRange = fourthRange = fifthRange = sixRange = seventhRange = eighthRange = 0
    for i in range(0, len(pPopulation)):
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
            eighthRange += 1
    return firstRange, secondRange, thirdRange, fourthRange, fifthRange, sixRange, seventhRange, eighthRange


def createChromosomeRepresentation(pSectorList):
    for sector in pSectorList:
        if sector.getSectorNumber() == 18:
            print()
        numberOfCombinations = 2 ** Constants.AMOUNT_OF_BITS
        populationPerRange = countPopulation(sector.getPopulation())
        totalPopulation = sum(populationPerRange)
        endOfLastRange = 0
        ranges = []
        for amountOfPopulationInRange in populationPerRange:
            percentageForDistribution = amountOfPopulationInRange / totalPopulation
            numberOfCombinationsForRange = numberOfCombinations * percentageForDistribution
            ranges += [[endOfLastRange, endOfLastRange + numberOfCombinationsForRange - 1]]
            if numberOfCombinationsForRange != 0:
                endOfLastRange = numberOfCombinationsForRange
        print(sector.getSectorNumber(), ranges)


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
