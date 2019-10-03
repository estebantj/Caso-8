from PIL import Image


def openImage(path):
    newImage = Image.open(path)
    return newImage


def main():
    path = ""
    image = openImage(path)
    image.show()
