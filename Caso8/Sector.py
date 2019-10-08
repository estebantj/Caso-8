import random


class Sector:
    def __init__(self, pCoodinatesSamples):
        self.__coordinatesSamples = pCoodinatesSamples
        self.__colorsSamples = []
        self.__whiteSamples = []
        self.__sectorNumber = 0
        self.__whitePercentaje = 0
        self.__nonWhitePercentaje = 0
        # self.__adjacency = 0

    def separateColorsSamples(self):
        for color in self.__colorsSamples:
            if color.isWhite():
                self.__whiteSamples += [color]

    def setColorSamples(self, pColorSamples):
        self.__colorsSamples = pColorSamples

    def setSectorNumber(self, pSectorNumber):
        self.__sectorNumber = pSectorNumber

    def getSectorNumber(self):
        return self.__sectorNumber

    def setWhitePercentaje(self, pWhitePercentaje):
        self.__whitePercentaje = pWhitePercentaje
        self.__nonWhitePercentaje = 100 - pWhitePercentaje

    def getWhitePercentaje(self):
        return self.__whitePercentaje

    def getColorSample(self):
        return self.__colorsSamples

    def getCoordinateSamples(self):
        return self.__coordinatesSamples

    def getRandomColorSample(self):
        return self.__colorsSamples[random.randint(0, len(self.__colorsSamples) - 1)]

    def __str__(self):
        return "Sector Number: " + str(self.__sectorNumber)


def getSectorWithTheLowestPercentageOfWhite(pSectorsList, pAdjacencyList):
    sectorWithTheLowestWhitePercentage = pSectorsList[pAdjacencyList[0]]
    for adjacentSectorIndex in range(1, len(pAdjacencyList) - 1):
        adjacentSector = pSectorsList[adjacentSectorIndex]
        if adjacentSector.getWhitePercentaje() < sectorWithTheLowestWhitePercentage.getWhitePercentaje():
            sectorWithTheLowestWhitePercentage = adjacentSector
    return sectorWithTheLowestWhitePercentage
