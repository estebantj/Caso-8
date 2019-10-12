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
            sector.sortNonWhiteColorsSamplesByBothCoordinates()
            colorSampleAtUpperLeftCorner = sector.getNonWhiteSamples()[0]
            colorSampleAtLowerRightCorner = sector.getNonWhiteSamples()[sector.getLenOfNonWhiteSamples() - 1]
            polygonPoints += [str(colorSampleAtUpperLeftCorner.getXCoordinate()) + "," + str(colorSampleAtUpperLeftCorner.getYCoordinate())]

            sectorYRange = sector.getYRange()
            sector.sortNonWhiteColorsSamplesByYCoordinate()
            lineIncrease = 10
            for yCoordinate in range(sectorYRange[0], sectorYRange[1], lineIncrease):
                point = sector.searchPointByYCoordinate(yCoordinate)
                if point is not None:
                    polygonPoints += [str(point.getXCoordinate()) + "," + str(point.getYCoordinate())]
            polygonPoints += [str(colorSampleAtLowerRightCorner.getXCoordinate()) + "," + str(colorSampleAtLowerRightCorner.getYCoordinate())]

            sector.reverseColorsOrder()
            for yCoordinate in range(sectorYRange[1], sectorYRange[0], -lineIncrease):
                point = sector.searchPointByYCoordinate(yCoordinate)
                if point is not None:
                    polygonPoints += [str(point.getXCoordinate()) + "," + str(point.getYCoordinate())]

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