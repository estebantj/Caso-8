import Constants
from Sector import getSectorWithTheLowestPercentageOfWhite


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
    """
    for sectorIndex, sector in enumerate(pSectorsList):
        if sector.getWhitePercentage() != 100:
            polygonPoints = []
            adjacencyList = adjMatrix.getAllAdjacency(sectorIndex)
            colorSample = sector.getRandomColorSample()
            polygonPoints += [str(colorSample.getXCoordinate()) + "," + str(colorSample.getYCoordinate())]

            while len(adjacencyList) != 0:
                sectorWithLowestWhitePercentage, sectorWithLowestWhitePercentageIndex = getSectorWithTheLowestPercentageOfWhite(pSectorsList, adjacencyList)
                if sectorWithLowestWhitePercentage.getWhitePercentage() != 100:
                    colorSample = sectorWithLowestWhitePercentage.getRandomColorSample()
                    polygonPoints += [str(colorSample.getXCoordinate()) + "," + str(colorSample.getYCoordinate())]
                    # print(adjacencyList)
                adjacencyList.remove(sectorWithLowestWhitePercentageIndex)
            if len(polygonPoints) >= 3:
                htmlPolygon = createHtmlPolygon(polygonPoints, colorSample)
                Constants.HTMLFILE.write(htmlPolygon)
        print(sector.getSectorNumber())
    """


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
