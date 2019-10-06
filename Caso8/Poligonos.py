class Polygon:
    def __init__(self):
        self.__pointsList = []


def polygonCreation(pSectorsList):
    polygonPoints = []
    adjacencyListPosition = []
    for listIndex in range(0, len(pSectorsList) - 1):
        adjacencyListPosition += [listIndex - 1]
        adjacencyListPosition += [listIndex + 1]
        adjacencyListPosition += [listIndex - 4]
        adjacencyListPosition += [listIndex + 4]
        adjacencyListPosition = [position for position in adjacencyListPosition if position in range(0, len(pSectorsList)-1)]
        print(adjacencyListPosition)


def createSVG(pointsList, pColor):
    colorRed = pColor.getRed()
    colorGreen = pColor.getGreen()
    colorBlue = pColor.getBlue()
    pointsString = ""
    for point in pointsList:
        pointsString += str(point) + " "
    svg = '<polygon points="' + pointsString + '" style="fill:rgb(' \
          + str(colorRed) + \
          ',' + str(colorGreen) + \
          ',' + str(colorBlue) + \
          ');stroke:black;stroke-width:1" />\n'
    return svg
