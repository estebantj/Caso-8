import math
import Constants
from Colors import Color
from PIL import Image, ImageDraw

# def polygonShapes(colorSampleAtTop, colorSampleAtLeft, colorSampleAtBottom, colorSampleAtRight):
#     polygonPoints = [colorSampleAtTop, colorSampleAtLeft, colorSampleAtBottom, colorSampleAtRight]
#     distances = []
#     for point in range (0, len(polygonPoints)):
#         pointI = polygonPoints[point]
#         if point != 3:
#             pointII = polygonPoints[point + 1]
#             distances += [math.hypot(pointII.getXCoordinate() - pointI.getXCoordinate(),
#                                      pointII.getYCoordinate() - pointI.getYCoordinate())]
#             print("Distancia entre el punto: ", str(pointI.getXCoordinate()), str(pointI.getYCoordinate()),
#                   " y ", str(pointII.getXCoordinate()), str(pointII.getYCoordinate()), " es:", str(distances[point]))
#         else:
#             pointII = polygonPoints[0]
#             distances += [math.hypot(pointII.getXCoordinate() - pointI.getXCoordinate(),
#                                      pointII.getYCoordinate() - pointI.getYCoordinate())]
#             print("Distancia entre el punto: ", str(pointI.getXCoordinate()), str(pointI.getYCoordinate()),
#                   " y ", str(pointII.getXCoordinate()), str(pointII.getYCoordinate()), " es:", str(distances[point]))
#     perimetro = 0
#     for elemento in range(0, len(distances)): perimetro += distances[elemento]
#     print("El Perimetro del poligono es: ", perimetro)
#     print("/////////////////////")

def addImageLines(image):
    numberOfSectionsPerLine = Constants.IMAGESIZE[0] / Constants.NUMBER_OF_LINES + 1
    linesList = []
    xPoint = Constants.IMAGESIZE[0] - 1
    imageForDrawing = ImageDraw.Draw(image)
    rgbImage = image.convert('RGB')
    sectorDivision = Constants.IMAGESIZE[0] // (Constants.NUMBER_OF_LINES + 1)

    for linesPerPixel in range(0, xPoint):
        # linesList += [[0, linesPerPixel],[xPoint, linesPerPixel]]
        colorList = []
        for moveRight in range(0, Constants.NUMBER_OF_LINES + 1):
            for pixelsPerLine in range(sectorDivision * moveRight, sectorDivision * (moveRight + 1)):
                r, g, b = rgbImage.getpixel((pixelsPerLine, linesPerPixel))
                newColor = Color(r, g, b, pixelsPerLine, linesPerPixel)
                colorList += [newColor]
            r, g, b = doColorPromedy(colorList);
            imageForDrawing.line([(sectorDivision * moveRight, linesPerPixel), (sectorDivision * (moveRight + 1), linesPerPixel)], fill = (r,g,b), width = 1)
    image.show()


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