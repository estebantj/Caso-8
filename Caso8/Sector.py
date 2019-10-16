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
        self.__bytesRange = []
        self.__target = []
        self.__bytesAverage = 0

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

    def setSectorNumber(self, pSectorNumber):
        self.__sectorNumber = pSectorNumber

    def setWhitePercentage(self):
        self.__whitePercentage = (self.__quantityOfWhiteSamples * 100) / (self.__quantityOfWhiteSamples + self.__quantityOfNonWhiteSamples)
        self.__nonWhitePercentage = 100 - self.__whitePercentage

    def getWhitePercentage(self):
        return self.__whitePercentage

    def getNonWhiteSamples(self):
        return self.__nonWhiteSamples

    def getAverageColor(self):
        r, g, b = 0, 0, 0
        for color in self.__nonWhiteSamples:
            r += color.getRed()
            g += color.getGreen()
            b += color.getBlue()
        r = int(r / len(self.__nonWhiteSamples))
        g = int(g / len(self.__nonWhiteSamples))
        b = int(b / len(self.__nonWhiteSamples))
        return Color(r, g, b, 0, 0)

    def setXRange(self, pXRange):
        self.__xRange = pXRange

    def setYRange(self, pYRange):
        self.__yRange = pYRange

    def getYRange(self):
        return self.__yRange

    def getXRange(self):
        return self.__xRange

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

    def getPopulation(self):
        return self.__population

    def getSectorNumber(self):
        return self.__sectorNumber

    def setBytesRange(self, pBytesRange):
        self.__bytesRange = pBytesRange

    def getBytesRange(self):
        return self.__bytesRange

    def setTarget(self, pColorRange):
        self.__target = self.__bytesRange[pColorRange - 1][1]

    def getTarget(self):
        return self.__target

    def setBytesAverage(self, pBytesAverage):
        self.__bytesAverage = pBytesAverage

    def getBytesAverage(self):
        return self.__bytesAverage


    def __str__(self):
        return "Sector Number: " + str(self.__sectorNumber)
