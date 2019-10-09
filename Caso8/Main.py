import Constants
from Sampling import *
from Polygons import *
from PIL import Image, ImageDraw

def openImage(pPath):
    newImage = Image.open(pPath)
    Constants.IMAGESIZE = newImage.size
    return newImage

def createSectorsLineDivision():
    image = openImage(Constants.IMAGES[1])
    imageWidth, imageHeight = image.size
    sectorsX = []
    sectorsY = []
    numberOfPixelsPerSectorX = imageWidth/(Constants.NUMBER_OF_LINES + 1)
    numberOfPixelsPerSectorY = imageHeight/(Constants.NUMBER_OF_LINES + 1)
    linePixelPositionX = 0
    linePixelPositionY = 0
    for actualNumberOfLines in range(0, Constants.NUMBER_OF_LINES):
        linePixelPositionX += numberOfPixelsPerSectorX
        sectorsX += [linePixelPositionX]
        linePixelPositionY += numberOfPixelsPerSectorY
        sectorsY += [linePixelPositionY]

    imageForDrawing = ImageDraw.Draw(image)
    for coordinateNumber in range(0, Constants.NUMBER_OF_LINES):
        x = sectorsX[coordinateNumber]
        y = sectorsY[coordinateNumber]
        htmlLine = '<line x1="' + str(x) + '" y1="0" x2="' + str(x) + '" y2="' + str(imageHeight) + '" stroke= '"black"' /> \n';
        Constants.HTMLFILE.write(htmlLine);
        htmlLine = '<line x1="0" y1="' + str(y)+ '" x2="' + str(imageWidth) + '" y2="' + str(y) + '" stroke= '"black"' /> \n';
        Constants.HTMLFILE.write(htmlLine);
        imageForDrawing.line([(x, 0), (x, imageHeight)], fill="red", width=1)
        imageForDrawing.line([(0, y), (imageWidth, y)], fill="red", width=1)

    #image.show()


if __name__ == "__main__" :
    image = openImage(Constants.IMAGES[1])
    sampleLists = createSectors()
    createColorsSamples(image, sampleLists)
    print()

    adjacencyGraph = createAdjacencyMatrix(sampleLists)
    # Una vez que se tienen las muestras y la matriz de adyacencias se crean los pogigonos
    Constants.HTMLFILE = open("View.html", "w")
    Constants.HTMLFILE.write(Constants.HTML1)

    createSectorsLineDivision()

    createSectors()
    polygonCreation(sampleLists, adjacencyGraph)

    # Create svg
    # pointsList = ["220,10", "300,210", "170,250", "123,234"]
    # htmlPolygon = createHtmlPolygon(pointsList, sampleLists[0].getColorSample()[0])
    # archivo.write(htmlPolygon)

    Constants.HTMLFILE.write(Constants.HTML2)
    Constants.HTMLFILE.close()

    print(adjacencyGraph.containsEdge(sampleLists[5].getSectorNumber() - 1, sampleLists[0].getSectorNumber() - 1))
    print("Final")
