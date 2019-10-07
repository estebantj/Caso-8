class Sector:
    def __init__(self, pCoodinatesSamples):
        self.__coordinatesSamples = pCoodinatesSamples
        self.__colorsSamples = []
        self.__sectorNumber = 0
        self.__whitePercentaje = 0
        self.__nonWhitePercentaje = 0
        # self.__adjacency = 0

    def setColorSamples(self, pColorSamples):
        self.__colorsSamples = pColorSamples

    def setSectorNumber(self, pSectorNumber):
        self.__sectorNumber = pSectorNumber

    def getSectorNumber(self):
        return self.__sectorNumber

    def setWhitePercentaje(self, pWhitePercentaje):
        self.__whitePercentaje = pWhitePercentaje
        self.__nonWhitePercentaje = 100 - pWhitePercentaje

    def getColorSample(self):
        return self.__colorsSamples

    def getCoordinateSamples(self):
        return self.__coordinatesSamples

    def __str__(self):
        return "Sector Number: " + str(self.__sectorNumber)