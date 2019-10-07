import random
from Colors import Color
import Constants
from Sector import Sector
from AdjacencyMatrix import *


def createSample():
    sampleOfSectors = []
    pointX1 = pointY1 = 0
    pointX2 = pointY2 = 0
    sectorDivision = 256
    sectorNumber = 1
    for horizontalDisplacement in range(1, 5):
        pointX2 = pointY2
        pointY2 = sectorDivision * horizontalDisplacement
        for verticalDisplacement in range(1, 5):
            sectors = []
            pointX1 = pointY1
            pointY1 = sectorDivision * verticalDisplacement

            for creationOfSamples in range(0, Constants.NUMBERS_OF_SAMPLES_PER_SECTOR):
                xCoordinate = random.randint(pointX1, pointY1)
                yCoordinate = random.randint(pointX2, pointY2)
                if xCoordinate == Constants.IMAGESIZE[0]:
                    xCoordinate -= 1
                if yCoordinate == Constants.IMAGESIZE[1]:
                    yCoordinate -= 1
                sectors += [[xCoordinate, yCoordinate]]
            newSector = Sector(sectors)
            newSector.setSectorNumber(sectorNumber)
            sampleOfSectors += [newSector]
            sectorNumber += 1
        pointX1 = 0
        pointY1 = 0
    return sampleOfSectors


def createColorsSamples(image, sampleLists):
    rgb_im = image.convert('RGB')
    for eachSector in sampleLists:
        colorsList = []
        whiteSamples = 0
        nonWhiteSamples = 0
        for eachCoordinateSample in eachSector.getCoordinateSamples():
            r, g, b = 0, 0, 0
            try:
                r, g, b = rgb_im.getpixel((eachCoordinateSample[0], eachCoordinateSample[1]))
            except IndexError:
                print("BIG ASS ERROR")
                print((eachCoordinateSample[0], eachCoordinateSample[1]))
            sampleColor = Color(r, g, b, eachCoordinateSample[0], eachCoordinateSample[1])
            if sampleColor.isWhite():
                whiteSamples += 1
            else:
                nonWhiteSamples += 1
            colorsList += [sampleColor]
        eachSector.setColorSamples(colorsList)
        eachSector.separateColorsSamples()
        whitePercentaje = (whiteSamples * 100) / Constants.NUMBERS_OF_SAMPLES_PER_SECTOR
        eachSector.setWhitePercentaje(whitePercentaje)


def createAdjacencyMatrix(sampleLists):
    # horizontalList = []
    # finalList = []
    # for sepateBySector in range(0, len(sampleLists)):
    #     if (sepateBySector + 1) % 4 != 0:
    #         # horizontalList += [Sector.getCoordinateSamples(sampleLists[sepateBySector])]
    #         horizontalList += [sepateBySector]
    #     else:
    #         # horizontalList += [Sector.getCoordinateSamples(sampleLists[sepateBySector])]
    #         horizontalList += [sepateBySector]
    #         finalList += [horizontalList]
    #         horizontalList = []
    g = Graph(len(sampleLists))
    for adjacencyBySector in range(0, len(sampleLists)):
        for adjacencySectorBySector in range(0, len(sampleLists)):
            if adjacencyBySector != adjacencySectorBySector:
                # print("Nodo: ", adjacencyBySector, " Valor: ", adjacencySectorBySector)
                if (adjacencyBySector - 1) == adjacencySectorBySector and (adjacencyBySector) % 4 != 0:
                    g.addEdge(adjacencyBySector, adjacencySectorBySector)
                elif (adjacencyBySector + 1) == adjacencySectorBySector and (adjacencyBySector + 1) % 4 != 0:
                    g.addEdge(adjacencyBySector, adjacencySectorBySector)
                elif (adjacencyBySector - 3) == adjacencySectorBySector and (adjacencyBySector + 1) % 4 != 0:
                    g.addEdge(adjacencyBySector, adjacencySectorBySector)
                elif (adjacencyBySector + 3) == adjacencySectorBySector and (adjacencyBySector) % 4 != 0:
                    g.addEdge(adjacencyBySector, adjacencySectorBySector)
                elif (adjacencyBySector - 4) == adjacencySectorBySector:
                    g.addEdge(adjacencyBySector, adjacencySectorBySector)
                elif (adjacencyBySector + 4) == adjacencySectorBySector:
                    g.addEdge(adjacencyBySector, adjacencySectorBySector)
                elif (adjacencyBySector - 5) == adjacencySectorBySector:
                    g.addEdge(adjacencyBySector, adjacencySectorBySector)
                elif (adjacencyBySector + 5) == adjacencySectorBySector:
                    g.addEdge(adjacencyBySector, adjacencySectorBySector)
                # else:
                #     print("No sirvio")
        # print("---------------------")
    g.toString()
    return g
    # 1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16
    # adjacencyMatrix = [[[0],[1],[0],[0],[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],1
    #                    [[1],[0],[1],[0],[1],[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0]],2
    #                    [[0],[1],[0],[1],[0],[1],[1],[1],[0],[0],[0],[0],[0],[0],[0],[0]],3
    #                    [[0],[0],[1],[0],[0],[0],[1],[1],[0],[0],[0],[0],[0],[0],[0],[0]],4
    #                    [[1],[1],[0],[0],[0],[1],[0],[0],[1],[1],[0],[0],[0],[0],[0],[0]],5
    #                    [[1],[1],[1],[0],[1],[0],[1],[0],[1],[1],[1],[0],[0],[0],[0],[0]],6
    #                    [[0],[1],[1],[1],[0],[1],[0],[1],[0],[1],[1],[1],[0],[0],[0],[0]],7
    #                    [[0],[0],[1],[1],[0],[0],[1],[0],[0],[0],[1],[1],[0],[0],[0],[0]],8
    #                    [[0],[0],[0],[0],[1],[1],[0],[0],[0],[1],[0],[0],[1],[1],[0],[0]],9
    #                    [[0],[0],[0],[0],[1],[1],[1],[0],[1],[0],[1],[0],[1],[1],[1],[0]],10
    #                    [[0],[0],[0],[0],[0],[1],[1],[1],[0],[1],[0],[1],[0],[1],[1],[1]],11
    #                    [[0],[0],[0],[0],[0],[0],[1],[1],[0],[0],[1],[0],[0],[0],[1],[1]],12
    #                    [[0],[0],[0],[0],[0],[0],[0],[0],[1],[1],[0],[0],[0],[1],[0],[0]],13
    #                    [[0],[0],[0],[0],[0],[0],[0],[0],[1],[1],[1],[0],[1],[0],[1],[0]],14
    #                    [[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1],[1],[0],[1],[0],[1]],15
    #                    [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1],[0],[0],[1],[0]],16]
