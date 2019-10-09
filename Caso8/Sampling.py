import random
from Colors import Color
import Constants
from Sector import Sector
from AdjacencyMatrix import *


def createSectors():
    sampleOfSectors = []
    pointY1 = 0
    pointY2 = 0
    sectorDivision = int((Constants.IMAGESIZE[0] / (Constants.NUMBER_OF_LINES + 1)))
    sectorNumber = 1
    for horizontalDisplacement in range(1, Constants.NUMBER_OF_LINES + 2):
        pointX2 = pointY2
        pointY2 = sectorDivision * horizontalDisplacement
        for verticalDisplacement in range(1, Constants.NUMBER_OF_LINES + 2):
            pointX1 = pointY1
            pointY1 = sectorDivision * verticalDisplacement
            newSector = Sector()
            if pointY1 == Constants.IMAGESIZE[0]:
                pointY1 -= 1
            if pointY2 == Constants.IMAGESIZE[1]:
                pointY2 -= 1
            newSector.setXRange([pointX1, pointY1])
            newSector.setYRange([pointX2, pointY2])
            newSector.setSectorNumber(sectorNumber)
            newSector.createPossibleCoordinates()
            sampleOfSectors += [newSector]
            sectorNumber += 1
        pointY1 = 0
    return sampleOfSectors


def createColorsSamples(pImage, pSampleList):
    rgbImage = pImage.convert('RGB')
    numberOfIterations = Constants.PERCENTAGE_FOR_SAMPLES // Constants.PERCENTAGE_PER_ITERATION
    pixelsPerSector = (Constants.IMAGESIZE[0] * Constants.IMAGESIZE[1]) / Constants.NUMBER_OF_SECTORS
    numberOfColorSamples = pixelsPerSector * (Constants.PERCENTAGE_FOR_SAMPLES / 100)
    numberOfColorSamplesPerIteration = int(numberOfColorSamples // numberOfIterations)
    percentageReduction = 1 / numberOfIterations
    # Segun la cantidad de porcentaje que se quiere tomar de cada sector asi sera la cantidad de iteraciones
    for iterationNumber in range(0, numberOfIterations):
        # Por cada sector se saca un random para ver si se toman puntos o no
        # Al inicio cada sector tiene probabilidad 1
        for eachSector in pSampleList:
            if random.random() < eachSector.getSectorProbability():
                whiteSamples = 0
                nonWhiteSamples = 0
                for amountOfColorSamples in range(0, numberOfColorSamplesPerIteration):
                    randomCoordinateIndex, randomCoordinate = eachSector.getRandomCoordinate()
                    r, g, b = rgbImage.getpixel((randomCoordinate[0], randomCoordinate[1]))
                    newColor = Color(r, g, b, randomCoordinate[0], randomCoordinate[1])
                    if newColor.isWhite():
                        whiteSamples += 1
                    else:
                        nonWhiteSamples += 1
                    eachSector.deleteCoordinateByIndex(randomCoordinateIndex)
                    eachSector.addColorSample(newColor)
                if whiteSamples > nonWhiteSamples:
                    eachSector.reduceSectorProbability(percentageReduction)
    for eachSector in pSampleList:
        eachSector.setWhitePercentage()


"""
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
"""

def createAdjacencyMatrix(sampleLists):
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
    # g.toString()
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