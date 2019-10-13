import random
from Colors import Color


class Sector:
    def __init__(self):
        self.__possibleCoordinates = []
        self.__nonWhiteSamples = []
        self.__sectorNumber = 0
        self.__whitePercentage = 0
        self.__nonWhitePercentage = 0
        self.__xRange = []
        self.__yRange = []
        self.__sectorProbability = 1
        self.__quantityOfWhiteSamples = 0
        self.__quantityOfNonWhiteSamples = 0
        self.__population = []

    def addColorSample(self, pColorSample):
        if pColorSample.isWhite():
            self.__quantityOfWhiteSamples += 1
        else:
            self.__quantityOfNonWhiteSamples += 1
            self.__nonWhiteSamples += [pColorSample]

    def createPossibleCoordinates(self):
        for xCoordinate in range(self.__xRange[0], self.__xRange[1]):
            for yCoordinate in range(self.__yRange[0], self.__yRange[1]):
                self.__possibleCoordinates += [[xCoordinate, yCoordinate]]

    def sortNonWhiteColorsSamplesByXCoordinate(self):
        self.__nonWhiteSamples.sort(key=lambda x: x.getXCoordinate())

    def sortNonWhiteColorsSamplesByYCoordinate(self):
        self.__nonWhiteSamples.sort(key=lambda x: x.getYCoordinate())

    def sortNonWhiteColorsSamplesByBothCoordinates(self):
        self.__nonWhiteSamples.sort(key=lambda x: x.getYCoordinate() + x.getXCoordinate())

    def setSectorNumber(self, pSectorNumber):
        self.__sectorNumber = pSectorNumber

    def getSectorNumber(self):
        return self.__sectorNumber

    def setWhitePercentage(self):
        self.__whitePercentage = (self.__quantityOfWhiteSamples * 100) / (self.__quantityOfWhiteSamples + self.__quantityOfNonWhiteSamples)
        self.__nonWhitePercentage = 100 - self.__whitePercentage

    def getWhitePercentage(self):
        return self.__whitePercentage

    def getNonWhiteSamples(self):
        return self.__nonWhiteSamples

    def getRandomColorSample(self):
        return self.__nonWhiteSamples[random.randint(0, len(self.__nonWhiteSamples) - 1)]

    def getLenOfNonWhiteSamples(self):
        return len(self.__nonWhiteSamples)

    def getAverageColor(self):
        r, g, b = 0, 0, 0
        for color in self.__nonWhiteSamples:
            r += color.getRed()
            g += color.getGreen()
            b += color.getBlue()
        r = r / len(self.__nonWhiteSamples)
        g = g / len(self.__nonWhiteSamples)
        b = b / len(self.__nonWhiteSamples)
        return Color(r, g, b, 0, 0)

    def setXRange(self, pXRange):
        self.__xRange = pXRange

    def setYRange(self, pYRange):
        self.__yRange = pYRange

    def getYRange(self):
        return self.__yRange

    def getXRange(self):
        return self.__xRange

    def searchPointByYCoordinate(self, pY):
        for color in self.__nonWhiteSamples:
            if color.getYCoordinate() == pY:
                return color
        return None

    def reverseColorsOrder(self):
        self.__nonWhiteSamples.reverse()

    def getRandomCoordinate(self):
        randomCoordinateIndex = random.randint(0, len(self.__possibleCoordinates) - 1)
        return randomCoordinateIndex, self.__possibleCoordinates[randomCoordinateIndex]

    def deleteCoordinateByIndex(self, pCoordinateIndex):
        self.__possibleCoordinates.pop(pCoordinateIndex)

    def getSectorProbability(self):
        return self.__sectorProbability

    def reduceSectorProbability(self, pMinus):
        self.__sectorProbability -= pMinus

    def addIndividualToPopulation(self, pIndividual):
        self.__population += [pIndividual]

    def __str__(self):
        return "Sector Number: " + str(self.__sectorNumber)


def getSectorWithTheLowestPercentageOfWhite(pSectorsList, pAdjacencyList):
    sectorWithTheLowestWhitePercentage = pSectorsList[pAdjacencyList[0]]
    sectorIndex = pAdjacencyList[0]
    for adjacentSectorIndex in range(1, len(pAdjacencyList) - 1):
        adjacentSector = pSectorsList[adjacentSectorIndex]
        if adjacentSector.getWhitePercentage() < sectorWithTheLowestWhitePercentage.getWhitePercentage():
            sectorWithTheLowestWhitePercentage = adjacentSector
            sectorIndex = pAdjacencyList[adjacentSectorIndex]
    return sectorWithTheLowestWhitePercentage, sectorIndex