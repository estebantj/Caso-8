import Constants
from Colors import Color
from PIL import Image, ImageDraw
import random

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
        newChromosome = 0
        firstParentColor = self.__color
        secondParentColor = pLine2.getColor()
        newColorRed = int((firstParentColor.getRed() + secondParentColor.getRed()) / 2)
        newColorGreen = int((firstParentColor.getGreen() + secondParentColor.getGreen()) / 2)
        newColorBlue = int((firstParentColor.getBlue() + secondParentColor.getBlue()) / 2)
        child = line(firstCoordinate, secondCoordinate, [newColorRed, newColorGreen, newColorBlue], self.__sector)
        child.setChromosome(newChromosome)
        return child

    def mutate(self):
        randomBit = random.randint(0, Constants.AMOUNT_OF_BITS)
        binaryNumberString = ""
        for i in range(0, Constants.AMOUNT_OF_BITS):
            if i != randomBit:
                binaryNumberString += "0"
            else:
                binaryNumberString += "1"
        binaryNumber = int(binaryNumberString, 2)

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
                for pixelsPerLine in range(sector.getXRange()[0], sector.getXRange()[1]):
                    r, g, b = rgbImage.getpixel((pixelsPerLine, amountOfLines))
                    newColor = Color(r, g, b, pixelsPerLine, amountOfLines)
                    if not newColor.isWhite():
                        colorList += [newColor]
                if colorList != []:
                    r, g, b = doColorPromedy(colorList)
                    lines = line([sector.getXRange()[0], amountOfLines],
                                 [sector.getXRange()[1], amountOfLines], [r, g, b], sector)
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
            geneticAlgorithm(sector.getPopulation(), ranges)

def geneticAlgorithm(pPopulation, pCromosomeRepresentation):
    actualPopulation = pPopulation
    for generation in range(0, Constants.NUMBER_OF_GENERATIONS):
        # Primero se calcula el "fitness" de cada individuo
        if len(actualPopulation) > 0:
            fitnessFunction(actualPopulation)
        else:
            print("Ya no hay poblacion con la que trabajar")
            break
        # Luego se ordena la poblacion segun su "fitness"
        for individual in actualPopulation:
            if individual.getFitness() == 1:
                actualPopulation += actualPopulation[individual]
        print("Tamaño de la poblacion actual: ", len(actualPopulation))
        # Un 10% pasa automaticamente a la siguiente generacion
        s = int((10 * len(actualPopulation)) / 100)
        newGeneration = []
        newGeneration.extend(actualPopulation[:s])
        for _ in range(0, int(len(actualPopulation)/2 - 1)):
            parent1 = random.choice(actualPopulation)
            parent2 = random.choice(actualPopulation)
            child = parent1.mate(parent2)
            newGeneration.append(child)
        actualPopulation = newGeneration
    print("-----------------")

def fitnessFunction(pPopulation):
    sector = pPopulation[0].getSector()  # <------ Problema Aqui
    sectorBytesRange = sector.getBytesRange()
    sectorTarget = sector.getTarget()
    sectorAverage = sector.getBytesAverage()
    AVG = int(sectorAverage / sectorTarget[1])
    for individual in pPopulation:
        chromosome = individual.getChromosome()
        if chromosome != None:
            x = int(abs(chromosome - sectorTarget[0]) / sectorTarget[1])
            if AVG + x < AVG:
                individual.setFitness(1)

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