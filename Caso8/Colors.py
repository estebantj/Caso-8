"""
    Clase utilizada para guardar los colores tomados aleatoriamente de la imagen
"""

class Colors:
    def __init__(self, pRed, pGreen, pBlue):
        self.__red = pRed
        self.__green = pGreen
        self.__blue = pBlue

    def getRed(self):
        return self.__red

    def getGreen(self):
        return self.__green

    def getBlue(self):
        return self.__blue
