from Sector import getSectorWithTheLowestPercentageOfWhite


class Polygon:
    def __init__(self):
        self.__pointsList = []


def polygonCreation(pSectorsList, adjMatrix):
    for sectorIndex, sector in enumerate(pSectorsList):
        if sector.getWhitePercentaje() != 0:
            polygonPoints = []
            adjacencyList = adjMatrix.getAllAdjacencies(sectorIndex)
            colorSample = sector.getRandomColorSample()
            polygonPoints += [str(colorSample.getXCoordinate) + "," + str(colorSample.getYCoordinate())]
            while len(adjacencyList) != 0 and len(polygonPoints) < 3:
                sectorWithLowestWhitePercentage = getSectorWithTheLowestPercentageOfWhite(pSectorsList, adjacencyList)
                if sectorWithLowestWhitePercentage.getWhitePercentaje() != 100:
                    colorSample = sectorWithLowestWhitePercentage.getRandomColorSample()
                    polygonPoints += [str(colorSample.getXCoordinate) + "," + str(colorSample.getYCoordinate())]
                    print(adjacencyList)
                adjacencyList.remove(sectorWithLowestWhitePercentage.getSectorNumber() - 1)

            if len(polygonPoints) >= 3:
                htmlPolygon = createHtmlPolygon(polygonPoints, colorSample)


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
