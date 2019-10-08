import random
from Colors import Color


class Sector:
    def __init__(self, pCoodinatesSamples):
        self.__coordinatesSamples = pCoodinatesSamples
        self.__colorsSamples = []
        self.__nonWhiteSamples = []
        self.__sectorNumber = 0
        self.__whitePercentaje = 0
        self.__nonWhitePercentaje = 0
        # self.__adjacency = 0

    def separateColorsSamples(self):
        for color in self.__colorsSamples:
            if not color.isWhite():
                self.__nonWhiteSamples += [color]

    def sortNonWhiteColoSamplesByXCoordinate(self):
        self.__nonWhiteSamples.sort(key=lambda x: x.getXCoordinate())


    def sortNonWhiteColoSamplesByYCoordinate(self):
        self.__nonWhiteSamples.sort(key=lambda x: x.getYCoordinate())

    def setColorSamples(self, pColorSamples):
        self.__colorsSamples = pColorSamples

    def setSectorNumber(self, pSectorNumber):
        self.__sectorNumber = pSectorNumber

    def getSectorNumber(self):
        return self.__sectorNumber

    def setWhitePercentaje(self, pWhitePercentaje):
        self.__whitePercentaje = pWhitePercentaje
        self.__nonWhitePercentaje = 100 - pWhitePercentaje

    def getWhitePercentage(self):
        return self.__whitePercentaje

    def getColorSamples(self):
        return self.__colorsSamples

    def getNonWhiteSamples(self):
        return self.__nonWhiteSamples

    def getCoordinateSamples(self):
        return self.__coordinatesSamples

    def getRandomColorSample(self):
        return self.__nonWhiteSamples[random.randint(0, len(self.__nonWhiteSamples) - 1)]

    def getColorPromedy(self):
        r, g, b = 0, 0, 0
        for color in self.__nonWhiteSamples:
            r += color.getRed()
            g += color.getGreen()
            b += color.getBlue()
        r = r/len(self.__nonWhiteSamples)
        g = g / len(self.__nonWhiteSamples)
        b = b / len(self.__nonWhiteSamples)
        return Color(r, g, b, 0 ,0)

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
