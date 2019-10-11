import Constants


class Polygon:
    def __init__(self):
        self.__pointsList = []


def polygonCreation(pSectorsList):
    for sectorIndex, sector in enumerate(pSectorsList):
        if sector.getWhitePercentage() != 100:
            polygonPoints = []
            sector.sortNonWhiteColorsSamplesByXCoordinate()
            colorSampleAtLeft = sector.getNonWhiteSamples()[0]
            colorSampleAtRight = sector.getNonWhiteSamples()[len(sector.getNonWhiteSamples()) - 1]
            sector.sortNonWhiteColorsSamplesByYCoordinate()
            colorSampleAtTop = sector.getNonWhiteSamples()[0]
            colorSampleAtBottom = sector.getNonWhiteSamples()[len(sector.getNonWhiteSamples()) - 1]

            polygonPoints += [str(colorSampleAtTop.getXCoordinate()) + "," + str(colorSampleAtTop.getYCoordinate())]
            polygonPoints += [str(colorSampleAtLeft.getXCoordinate()) + "," + str(colorSampleAtLeft.getYCoordinate())]

            polygonPoints += [str(colorSampleAtBottom.getXCoordinate()) + "," + str(colorSampleAtBottom.getYCoordinate())]
            polygonPoints += [str(colorSampleAtRight.getXCoordinate()) + "," + str(colorSampleAtRight.getYCoordinate())]

            averageColor = sector.getAverageColor()
            htmlPolygon = createHtmlPolygon(polygonPoints, averageColor)
            Constants.HTMLFILE.write(htmlPolygon)


def polygonCreation2(pSectorsList):
    for sectorIndex, sector in enumerate(pSectorsList):
        if sector.getWhitePercentage() != 100:
            polygonPoints = []
            sector.sortNonWhiteColorsSamplesByXCoordinate()
            colorSampleAtLeft = sector.getNonWhiteSamples()[0]
            colorSampleAtRight = sector.getNonWhiteSamples()[sector.getLenOfNonWhiteSamples() - 1]
            sector.sortNonWhiteColorsSamplesByYCoordinate()
            colorSampleAtTop = sector.getNonWhiteSamples()[0]
            colorSampleAtBottom = sector.getNonWhiteSamples()[sector.getLenOfNonWhiteSamples() - 1]

            sector.sortNonWhiteColorsSamplesByBothCoordinates()
            colorSampleAtUpperLeftCorner = sector.getNonWhiteSamples()[0]
            colorSampleAtLowerRightCorner = sector.getNonWhiteSamples()[sector.getLenOfNonWhiteSamples() - 1]

            polygonPoints += [str(colorSampleAtTop.getXCoordinate()) + "," + str(colorSampleAtTop.getYCoordinate())]
            polygonPoints += [str(colorSampleAtUpperLeftCorner.getXCoordinate()) + "," + str(colorSampleAtUpperLeftCorner.getYCoordinate())]
            polygonPoints += [str(colorSampleAtLeft.getXCoordinate()) + "," + str(colorSampleAtLeft.getYCoordinate())]

            polygonPoints += [str(colorSampleAtBottom.getXCoordinate()) + "," + str(colorSampleAtBottom.getYCoordinate())]
            polygonPoints += [str(colorSampleAtLowerRightCorner.getXCoordinate()) + "," + str(colorSampleAtLowerRightCorner.getYCoordinate())]
            polygonPoints += [str(colorSampleAtRight.getXCoordinate()) + "," + str(colorSampleAtRight.getYCoordinate())]

            averageColor = sector.getAverageColor()
            htmlPolygon = createHtmlPolygon(polygonPoints, averageColor)
            Constants.HTMLFILE.write(htmlPolygon)


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