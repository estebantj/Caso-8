import math
import Constants

def polygonShapes(colorSampleAtTop, colorSampleAtLeft, colorSampleAtBottom, colorSampleAtRight):
    polygonPoints = [colorSampleAtTop, colorSampleAtLeft, colorSampleAtBottom, colorSampleAtRight]
    count = 1
    for point in range (0, len(polygonPoints)):
        if count != 3:
            distances = math.hypot(polygonPoints[count].getXCoordinate() - polygonPoints[count - 1].getXCoordinate(), polygonPoints[count].getYCoordinate() - polygonPoints[count - 1].getYCoordinate())
            print("Distancia entre el punto: ", str(polygonPoints[count - 1].getXCoordinate()), str(polygonPoints[count - 1].getYCoordinate()), " y ", str(polygonPoints[count].getXCoordinate()), str(polygonPoints[count].getYCoordinate()), " es:", str(distances))
            count += 1
        else:
            distances = math.hypot(polygonPoints[0].getXCoordinate() - polygonPoints[count].getXCoordinate(), polygonPoints[0].getYCoordinate() - polygonPoints[count].getYCoordinate())
            print("Distancia entre el punto: ", str(polygonPoints[count].getXCoordinate()), str(polygonPoints[count].getYCoordinate()), " y ", str(polygonPoints[0].getXCoordinate()), str(polygonPoints[0].getYCoordinate()), " es:", str(distances))
    print("/////////////////////")