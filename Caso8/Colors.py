"""
    Clase utilizada para guardar los colores tomados aleatoriamente de la imagen
"""


class Color:
    def __init__(self, pRed, pGreen, pBlue):
        self.__red = pRed
        self.__green = pGreen
        self.__blue = pBlue

    def isWhite(self):
        return self.__red == 255 and self.__green == 255 and self.__blue == 255

    def __str__(self):
        return "R: "+str(self.__red)+" G: "+str(self.__green)+" B: "+str(self.__blue)

    def getRed(self):
        return self.__red

    def getGreen(self):
        return self.__green

    def getBlue(self):
        return self.__blue
