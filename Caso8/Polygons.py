import Constants
from Sector import getSectorWithTheLowestPercentageOfWhite
from Shapes import polygonShapes

class Polygon:
    def __init__(self):
        self.__pointsList = []

def polygonCreation(pSectorsList, adjMatrix):

    for sectorIndex, sector in enumerate(pSectorsList):
        if sector.getWhitePercentage() != 100:
            polygonPoints = []
            sector.sortNonWhiteColoSamplesByXCoordinate()
            colorSampleAtLeft = sector.getNonWhiteSamples()[0]
            colorSampleAtRight = sector.getNonWhiteSamples()[len(sector.getNonWhiteSamples()) - 1]
            sector.sortNonWhiteColoSamplesByYCoordinate()
            colorSampleAtTop = sector.getNonWhiteSamples()[0]
            colorSampleAtBottom = sector.getNonWhiteSamples()[len(sector.getNonWhiteSamples()) - 1]

            polygonPoints += [str(colorSampleAtTop.getXCoordinate()) + "," + str(colorSampleAtTop.getYCoordinate())]
            polygonPoints += [str(colorSampleAtLeft.getXCoordinate()) + "," + str(colorSampleAtLeft.getYCoordinate())]

            polygonPoints += [str(colorSampleAtBottom.getXCoordinate()) + "," + str(colorSampleAtBottom.getYCoordinate())]
            polygonPoints += [str(colorSampleAtRight.getXCoordinate()) + "," + str(colorSampleAtRight.getYCoordinate())]

            averageColor = sector.getColorPromedy()
            htmlPolygon = createHtmlPolygon(polygonPoints, averageColor)
            Constants.HTMLFILE.write(htmlPolygon)
            polygonShapes(colorSampleAtTop, colorSampleAtLeft, colorSampleAtBottom, colorSampleAtRight)

def createHtmlPolygon(pointsList, pColor):
    colorRed = pColor.getRed()
    colorGreen = pColor.getGreen()
    colorBlue = pColor.getBlue()
    pointsString = ""
    for point in pointsList:
        pointsString += str(point) + " "
    htmlPolygon = '<polygon points="' + pointsString + '" style="fill:rgb(' \
                  + str(colorRed) + \
                  ',' + str(colorGreen) + \
                  ',' + str(colorBlue) + \
                  ');stroke:black;stroke-width:1" />\n'
    return htmlPolygon