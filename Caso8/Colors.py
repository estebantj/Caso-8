"""
    Clase utilizada para guardar los colores tomados aleatoriamente de la imagen
"""

class Color:
    def __init__(self, pRed, pGreen, pBlue, pXCoordinate, pYCoordinate):
        self.__red = pRed
        self.__green = pGreen
        self.__blue = pBlue
        self.__xCoordinate = pXCoordinate
        self.__yCoordinate = pYCoordinate

    def isWhite(self):
        return self.__red > 245 and self.__green > 245 and self.__blue > 245

    def __str__(self):
        return "R: "+str(self.__red)+" G: "+str(self.__green)+" B: "+str(self.__blue)

    def getRed(self):
        return self.__red

    def getGreen(self):
        return self.__green

    def getBlue(self):
        return self.__blue

    def getXCoordinate(self):
        return self.__xCoordinate

    def getYCoordinate(self):
        return self.__yCoordinate