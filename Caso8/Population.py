import Constants
from Colors import Color
from PIL import Image, ImageDraw
import random
from Polygons import createHtmlPolygon

listOfLines = []

class line:
    def __init__(self, pFirstCoordinate, pSecondCoordinate, pColor, pSector):
        self.__firstCoordinate = pFirstCoordinate
        self.__secondCoordinate = pSecondCoordinate
        self.__color = Color(pColor[0], pColor[1], pColor[2], 0, 0)
        self.__colorRange = getColorRange(pColor[0], pColor[1], pColor[2])
        self.__sector = pSector
        self.__fitness = 0
        self.__chromosome = None

    def getFirstPoint(self):
        return self.__firstCoordinate

    def getSecondPoint(self):
        return self.__secondCoordinate

    def getColorRange(self):
        return self.__colorRange

    def mate(self, pLine2):
        firstCoordinate = random.choice([self.__firstCoordinate, pLine2.getFirstPoint()])
        secondCoordinate = random.choice([self.__secondCoordinate, pLine2.getSecondPoint()])
        firstParentChromosome = self.__chromosome
        secondParentChromosome = pLine2.getChromosome()
        byteTransformation = "0" + str(Constants.AMOUNT_OF_BITS) + "b"
        firstParentInBytes = format(firstParentChromosome, byteTransformation)
        secondParentInBytes = format(secondParentChromosome, byteTransformation)
        amountOfBitsForFirstParent = random.randint(1, 7)
        firstParentPart = ""
        secondParentPart = ""
        for bitsPerFirstParent in range(0, amountOfBitsForFirstParent):
            firstParentPart += str(firstParentInBytes[bitsPerFirstParent])

        for bitsPerSecondParent in range(amountOfBitsForFirstParent, len(secondParentInBytes)):
            secondParentPart += str(secondParentInBytes[bitsPerSecondParent])

        # print("First Parent --------------------------")
        # print(firstParentInBytes)
        # print(firstParentPart)
        # print("Second Parent --------------------------")
        # print(secondParentInBytes)
        # print(secondParentPart)
        # print(int(firstParentPart + secondParentPart, 2))
        newChromosome = int(firstParentPart + secondParentPart, 2)
        firstParentColor = self.__color
        secondParentColor = pLine2.getColor()
        sectorAverageColor = self.__sector.getAverageColor()
        newColorRed = int((firstParentColor.getRed() + secondParentColor.getRed() + sectorAverageColor.getRed()) / 3)
        newColorGreen = int((firstParentColor.getGreen() + secondParentColor.getGreen() + sectorAverageColor.getGreen()) / 3)
        newColorBlue = int((firstParentColor.getBlue() + secondParentColor.getBlue() + sectorAverageColor.getBlue()) / 3)
        child = line(firstCoordinate, secondCoordinate, [newColorRed, newColorGreen, newColorBlue], self.__sector)
        child.setChromosome(newChromosome)
        return child

    def mutate(self):
        probability = random.random()
        if 0 < probability < 0.07:
            randomBit = random.randint(0, Constants.AMOUNT_OF_BITS)
            binaryNumberString = ""
            for i in range(0, Constants.AMOUNT_OF_BITS):
                if i != randomBit:
                    binaryNumberString += "0"
                else:
                    binaryNumberString += "1"
            binaryNumber = int(binaryNumberString, 2)
            self.__chromosome = self.__chromosome ^ binaryNumber

    def setFitness(self, pFitness):
        self.__fitness = pFitness

    def getFitness(self):
        return self.__fitness

    def setChromosome(self, pChromosome):
        self.__chromosome = pChromosome

    def getChromosome(self):
        return self.__chromosome

    def getSector(self):
        return self.__sector

    def getColor(self):
        return self.__color

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
        return 9

def countPopulation(pPopulation):
    firstRange = secondRange = thirdRange = fourthRange = fifthRange = sixRange = seventhRange = eighthRange = nineRange = 0
    for i in range(0, len(pPopulation)):
        revisar = pPopulation[i].getColorRange()
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
        elif revisar == 9:
            nineRange += 1
    return firstRange, secondRange, thirdRange, fourthRange, fifthRange, sixRange, seventhRange, eighthRange, nineRange

def createPopulationPerSector(pSectorList, pImage):
    global listOfLines
    rgbImage = pImage.convert('RGB')
    for sector in pSectorList:
        if sector.getWhitePercentage() != 100:
            for amountOfLines in range(sector.getYRange()[0], sector.getYRange()[1], 2):
                colorList = []
                startCoordinate = None
                endCoordinate = None
                for pixelsPerLine in range(sector.getXRange()[0], sector.getXRange()[1]):
                    r, g, b = rgbImage.getpixel((pixelsPerLine, amountOfLines))
                    newColor = Color(r, g, b, pixelsPerLine, amountOfLines)
                    if not newColor.isWhite():
                        if startCoordinate is None:
                            startCoordinate = [pixelsPerLine, amountOfLines]
                        endCoordinate = [pixelsPerLine, amountOfLines]
                        colorList += [newColor]
                if colorList != []:
                    r, g, b = doColorPromedy(colorList)
                    lines = line(startCoordinate, endCoordinate, [r, g, b], sector)
                    listOfLines += [lines]
                    sector.addIndividualToPopulation(lines)

def createChromosomeRepresentation(pSectorList):
    numberOfCombinations = 2 ** Constants.AMOUNT_OF_BITS
    for sector in pSectorList:
        if sector.getWhitePercentage() != 100 and len(sector.getPopulation()) != 0:
            populationPerRange = countPopulation(sector.getPopulation())
            totalPopulation = sum(populationPerRange)
            endOfLastRange = 0
            ranges = []
            for amountOfPopulationInRange in populationPerRange:
                if amountOfPopulationInRange > 0:
                    percentageForDistribution = amountOfPopulationInRange / totalPopulation
                    numberOfCombinationsForRange = numberOfCombinations * percentageForDistribution
                    Range = [percentageForDistribution, [endOfLastRange, int(round(endOfLastRange + numberOfCombinationsForRange - 1))]]
                    ranges += [Range]
                    if numberOfCombinationsForRange != 0:
                        endOfLastRange = int(round(endOfLastRange + numberOfCombinationsForRange))
                else:
                    Range = [0, [0, 0]]
                    ranges += [Range]
            # Se le da al sector los rangos de bytes y ademas se define en que rango esta el target del sector
            sector.setBytesRange(ranges)
            sectorAverageColor = sector.getAverageColor()
            sectorColorRange = getColorRange(sectorAverageColor.getRed(), sectorAverageColor.getGreen(), sectorAverageColor.getBlue())
            sector.setTarget(sectorColorRange)
            ranges.sort(key=lambda x: x[0])
            # Ahora a cada linea se le da un numero aleatorio segun su rango
            AVG = 0
            for individual in sector.getPopulation():
                randomNumber = random.random()
                Sum = 0
                for rangeIndex in range(0, len(ranges)):
                    actualPercentaje = ranges[rangeIndex][0]
                    if Sum <= randomNumber < Sum + ranges[rangeIndex][0]:
                        Range = ranges[rangeIndex][1]
                        chromosome = random.randint(Range[0], Range[1])
                        AVG += chromosome
                        individual.setChromosome(chromosome)
                    Sum += ranges[rangeIndex][0]
            AVG = AVG // totalPopulation
            sector.setBytesAverage(AVG)
            # print("Sector actual:", sector.getSectorNumber())
            geneticAlgorithm(sector.getPopulation(), ranges)

def createPolygonFromPopulation(pPopulation):
    referencesCopy = []
    referencesCopy.extend(pPopulation)
    polygonPoints = []
    colors = []
    for i in range(0,6):
        lineIndex = random.randint(0, len(referencesCopy) - 1)
        line = referencesCopy[lineIndex]
        referencesCopy.pop(lineIndex)
        colors += [line.getColor()]
        lineFirstCoordinate = line.getFirstPoint()
        lineSecondCoordinate = line.getSecondPoint()

        if lineFirstCoordinate[0] < lineSecondCoordinate[0]:
            pointXCoordinate = random.randint(lineFirstCoordinate[0], lineSecondCoordinate[0])
        elif lineFirstCoordinate[0] > lineSecondCoordinate[0]:
            pointXCoordinate = random.randint(lineSecondCoordinate[0], lineFirstCoordinate[0])
        else:
            pointXCoordinate = lineFirstCoordinate[0]

        if lineFirstCoordinate[1] < lineSecondCoordinate[1]:
            pointYCoordinate = random.randint(lineFirstCoordinate[1], lineSecondCoordinate[1])
        elif lineFirstCoordinate[1] > lineSecondCoordinate[1]:
            pointYCoordinate = random.randint(lineSecondCoordinate[1], lineFirstCoordinate[1])
        else:
            pointYCoordinate = lineFirstCoordinate[1]
        polygonPoints += [str(pointXCoordinate) + "," + str(pointYCoordinate)]
        if len(referencesCopy) == 0:
            break

    averageColor = [0, 0, 0]
    for color in colors:
        averageColor[0] += color.getRed()
        averageColor[1] += color.getGreen()
        averageColor[2] += color.getBlue()
    averageColor[0] = int(averageColor[0] / len(colors))
    averageColor[1] = int(averageColor[1] / len(colors))
    averageColor[2] = int(averageColor[2] / len(colors))
    htmlPolygon = createHtmlPolygon(polygonPoints, Color(averageColor[0], averageColor[1], averageColor[2], 0, 0))
    Constants.HTMLFILE.write(htmlPolygon)


def geneticAlgorithm(pPopulation, pCromosomeRepresentation):
    for generation in range(0, Constants.NUMBER_OF_GENERATIONS):
        # Primero se calcula el "fitness" de cada individuo
        fitnessFunction(pPopulation)
        referencesCopy = []
        referencesCopy.extend(pPopulation)
        while len(referencesCopy)/10 > 2:
            firstParentIndex = random.randrange(0, len(referencesCopy))
            parent1 = referencesCopy[firstParentIndex]
            referencesCopy.pop(firstParentIndex)

            secondParentIndex = random.randrange(0, len(referencesCopy))
            parent2 = referencesCopy[secondParentIndex]
            referencesCopy.pop(secondParentIndex)

            child = parent1.mate(parent2)
            child.mutate()
            pPopulation.append(child)
        if len(pPopulation) == 0:
            # print("Ya no hay poblacion con la que trabajar")
            break
        createPolygonFromPopulation(pPopulation)
    # print("-----------------", len(pPopulation))

def fitnessFunction(pPopulation):
    sector = pPopulation[0].getSector()  # <------ Problema Aqui
    sectorBytesRange = sector.getBytesRange()
    sectorTarget = sector.getTarget()
    sectorAverage = sector.getBytesAverage()
    AVG = int(sectorAverage / sectorTarget[1])
    individualIndex = 0
    newPopulation = []
    while individualIndex < len(pPopulation):
        individual = pPopulation[individualIndex]
        chromosome = individual.getChromosome()
        x = int(abs(chromosome - sectorTarget[0]) / sectorTarget[1])
        if AVG + x > AVG:
            individual.setFitness(1)
            newPopulation += [individual]
            pPopulation.pop(individualIndex)
            if len(pPopulation) == 0:
                break
            AVG = int(sum(x.getChromosome() for x in pPopulation) / len(pPopulation) / sectorTarget[1])
        else:
            individualIndex += 1
    pPopulation = newPopulation

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