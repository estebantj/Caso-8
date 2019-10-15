import Constants
from Colors import Color
from PIL import Image, ImageDraw
import random

listOfLines = []


class line:
    def __init__(self, pFirstCoordinate, pSecondCoordinate, pColor, pSector):
        self.__firstCoordinate = pFirstCoordinate
        self.__secondCoordinate = pSecondCoordinate
        self.__color = pColor
        self.__colorRange = getColorRange(pColor[0], pColor[1], pColor[2])
        self.__sector = pSector
        self.__fitness = self.calculateFitness()
        self.__chromosome = None

    def getFirstPoint(self):
        return self.__firstCoordinate

    def getSecondPoint(self):
        return self.__secondCoordinate

    def getColorRange(self):
        return self.__colorRange

    def mate(self, pLine2):
        return line(self.__firstCoordinate, self.__secondCoordinate, self.__color, self.__sector)

    def calculateFitness(self):
        # La funcion toma el rango en que se encuentra el sector
        # Revisa la diferencia entre el rango de la linea y el sector, entre mas alto mas lejos
        sectorAverageColor = self.__sector.getAverageColor()
        sectorTarget = getColorRange(sectorAverageColor.getRed(), sectorAverageColor.getGreen(), sectorAverageColor.getBlue())
        fitness = abs(sectorTarget - self.__colorRange)
        return fitness

    def setFitness(self, pFitness):
        self.__fitness = pFitness

    def getFitness(self):
        return self.__fitness

    def setChromosome(self, pChromosome):
        self.__chromosome = pChromosome


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
    #elif (pRed >= 128 and pRed <= 245) and (pGreen >= 128 and pGreen <= 245) and (pBlue >= 128 and pBlue <= 245):
        #return 8
    elif pRed >= 128 and pGreen >= 128 and pBlue >= 128:
        return 8
    else:
        return 9


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
                    colorList += [newColor]
                r, g, b = doColorPromedy(colorList)
                lines = line([sector.getXRange()[0], amountOfLines],
                             [sector.getXRange()[1], amountOfLines], [r, g, b], sector)
                listOfLines += [lines]
                sector.addIndividualToPopulation(lines)

# def createPopulationPerSector2(pSectorList, pImage):
#     global listOfLines
#     numberOfSectionsPerLine = Constants.IMAGESIZE[0] / Constants.NUMBER_OF_LINES + 1
#     xPoint = Constants.IMAGESIZE[0] - 1
#     newImage = Image.new("RGB", (Constants.IMAGESIZE[0], Constants.IMAGESIZE[1]))
#     imageForDrawing = ImageDraw.Draw(newImage)
#     imageForColor = ImageDraw.Draw(pImage)
#     rgbImage = pImage.convert('RGB')
#     sectorDivision = Constants.IMAGESIZE[0] // (Constants.NUMBER_OF_LINES + 1)
#
#     for linesPerPixel in range(0, xPoint, 3):
#         for moveRight in range(0, Constants.NUMBER_OF_LINES + 1):
#             colorList = []
#             for pixelsPerLine in range(sectorDivision * moveRight, (sectorDivision * (moveRight + 1)) - 1):
#                 r, g, b = rgbImage.getpixel((pixelsPerLine, linesPerPixel))
#                 newColor = Color(r, g, b, pixelsPerLine, linesPerPixel)
#                 colorList += [newColor]
#             r, g, b = doColorPromedy(colorList)
#             imageForDrawing.line(
#                 [(sectorDivision * moveRight, linesPerPixel), (sectorDivision * (moveRight + 1) - 1, linesPerPixel)],
#                 fill=(r, g, b), width=1)
#             lines = line([sectorDivision * moveRight, linesPerPixel],
#                          [sectorDivision * (moveRight + 1) - 1, linesPerPixel], [r, g, b])
#             listOfLines += [lines]
#
#     print(len(listOfLines))
#     # pImage.show()
#     # newImage.show()
#     return listOfLines


# def createChromosomeRepresentation2(listOfLines):
#     # [[0, 1159], [0, 0], [1160, 1200], [1201, 1208], [1209, 1220], [1221, 1251], [0, 0], [1252, 4094]]
#     # [[0, 1159], [0, 0], [1160, 1200], [1201, 1208], [1209, 1220], [1221, 1251], [0, 0], [1252, 1667]]
#     populationPerRange = countPopulation(listOfLines)
#     numberOfCombinations = 2 ** Constants.AMOUNT_OF_BITS
#     totalPopulation = len(listOfLines)
#     for sector in range(0, len(listOfLines)):
#         endOfLastRange = 0
#         ranges = []
#         for amountOfPopulationInRange in populationPerRange:
#             if amountOfPopulationInRange > 0:
#                 percentageForDistribution = amountOfPopulationInRange / totalPopulation
#                 numberOfCombinationsForRange = numberOfCombinations * percentageForDistribution
#                 ranges += [[endOfLastRange, int(round(endOfLastRange + numberOfCombinationsForRange - 1))]]
#                 if numberOfCombinationsForRange != 0:
#                     endOfLastRange = int(round(endOfLastRange + numberOfCombinationsForRange))
#             else:
#                 ranges += [[0, 0]]
#     print(ranges)
#     return ranges


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


def createChromosomeRepresentation(pSectorList):
    numberOfCombinations = 2 ** Constants.AMOUNT_OF_BITS
    populationPerRange = countPopulation(pSectorList[0].getPopulation())
    totalPopulation = sum(populationPerRange)
    for sector in pSectorList:
        if sector.getWhitePercentage() != 100:
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
                for rangeIndex in range(0, len(ranges)-1):
                    actualPercentaje = ranges[rangeIndex][0]
                    if Sum <= randomNumber < Sum + ranges[rangeIndex][0]:
                        Range = ranges[rangeIndex][1]
                        chromosome = random.randint(Range[0], Range[1])
                        individual.setChromosome(chromosome)
                    Sum += ranges[rangeIndex][0]
            AVG = AVG // totalPopulation
            sector.setBytesAverage(AVG)
            if sector.getSectorNumber() == 28:
                print(sector.getSectorNumber(), ranges)
            geneticAlgorithm(sector.getPopulation(), ranges)


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


def fitnessFunction(pPopulation):
    sector = pPopulation[0].getSector()
    sectorBytesRange = sector.getBytesRange()
    sectorTarget = []
    for individual in pPopulation:
        pass


def geneticAlgorithm(pPopulation, pCromosomeRepresentation):
    actualPopulation = pPopulation
    for generation in range(0, Constants.NUMBER_OF_GENERATIONS):
        # Primero se calcula el "fitness" de cada individuo

        # Luego se ordena la poblacion segun su "fitness"
        actualPopulation.sort(key=lambda individual: individual.getFitness())
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