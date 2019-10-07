import Constants
from Sampling import *
from Polygons import *
from PIL import Image, ImageDraw


def openImage(pPath):
    newImage = Image.open(pPath)
    Constants.IMAGESIZE = newImage.size
    return newImage


def createSectors():
    image = openImage(Constants.IMAGES[0])
    imageWidth, imageHeight = image.size
    sectorsX = []
    sectorsY = []
    numberOfPixelsPerSectorX = imageWidth/(Constants.NUMBERS_OF_LINES + 1)
    numberOfPixelsPerSectorY = imageHeight/(Constants.NUMBERS_OF_LINES + 1)
    linePixelPositionX = 0
    linePixelPositionY = 0
    for actualNumberOfLines in range(0, Constants.NUMBERS_OF_LINES):
        linePixelPositionX += numberOfPixelsPerSectorX
        sectorsX += [linePixelPositionX]
        linePixelPositionY += numberOfPixelsPerSectorY
        sectorsY += [linePixelPositionY]

    imageForDrawing = ImageDraw.Draw(image)
    for coordinateNumber in range(0, Constants.NUMBERS_OF_LINES):
        x = sectorsX[coordinateNumber]
        y = sectorsY[coordinateNumber]
        imageForDrawing.line([(x, 0), (x, imageHeight)], fill="red", width=1)
        imageForDrawing.line([(0, y), (imageWidth, y)], fill="red", width=1)

    image.show()

    print(sectorsX)
    print(sectorsY)


if __name__ == "__main__" :
    image = openImage(Constants.IMAGES[0])
    #createSectors()
    sampleLists = createSample()
    #sampleLists.sort(key=lambda sector: sector.getSectorNumber(), reverse=False)
    # print("Size Lista: ", len(sampleLists))
    # for i in range(0, len(sampleLists)):
    #     print("Sector ", i + 1)
    #     print(Sector.getCoordinateSamples(sampleLists[i]))
    #     print("//////////////")

    createColorsSamples(image, sampleLists)
    adjacencyGraph = createAdjacencyMatrix(sampleLists)
    # Una vez que se tienen las muestras y la matriz de adyacencias se crean los pogigonos
    Constants.HTMLFILE = open("View.html", "w")
    Constants.HTMLFILE.write(Constants.HTML1)

    polygonCreation(sampleLists, adjacencyGraph)

    # Create svg
    #pointsList = ["220,10", "300,210", "170,250", "123,234"]
    #htmlPolygon = createHtmlPolygon(pointsList, sampleLists[0].getColorSample()[0])
    #archivo.write(htmlPolygon)

    Constants.HTMLFILE.write(Constants.HTML2)
    Constants.HTMLFILE.close()

    print(adjacencyGraph.containsEdge(sampleLists[5].getSectorNumber() - 1, sampleLists[0].getSectorNumber() - 1))
    print("Final")