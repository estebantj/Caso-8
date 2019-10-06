import random
from Colors import Color
import Constants
from Sector import Sector


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
            sampleColor = Color(r, g, b)
            if sampleColor.isWhite():
                whiteSamples +=1
            else:
                nonWhiteSamples += 1
            colorsList += [sampleColor]
        eachSector.setColorSamples(colorsList)
        whitePercentaje = (whiteSamples * 100) / Constants.NUMBERS_OF_SAMPLES_PER_SECTOR
        eachSector.setWhitePercentaje(whitePercentaje)


"""
def estimateWhiteColor(sectorsList):
    for sector in sectorsList:
        whiteSamples = 0
        nonWhiteSamples = 0
        for color in sector.getColorSample():
            if color.isWhite():
                whiteSamples += 1
            else:
                nonWhiteSamples += 1
        whitePercentaje = (whiteSamples * 100) / Constants.NUMBERS_OF_SAMPLES_PER_SECTOR
        sector.setWhitePercentaje(whitePercentaje)
        print("Sector white percentaje: ", whitePercentaje)
"""