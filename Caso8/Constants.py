IMAGES = ["firstImage.jpg", "secondImage.jpg", "thirdImage.jpg", "fourthImage.png", "beach.png", "guacamaya.png", "prueba.jpg", "colores.jpg"]
NUMBER_OF_LINES = 25
NUMBER_OF_SECTORS = (NUMBER_OF_LINES + 1) * (NUMBER_OF_LINES + 1)
NUMBERS_OF_SAMPLES_PER_SECTOR = 200
PERCENTAGE_FOR_SAMPLES = 50
PERCENTAGE_PER_ITERATION = 10
AMOUNT_OF_BITS = 5
NUMBER_OF_GENERATIONS = 10
IMAGESIZE = 0
HTMLFILE = None
HTML1 = " \
<html>\n \
    <head>\n \
        <style>\n \
            #base1 {\n \
                width : 1024px;\n \
                height: 1024px;\n \
                margin-left: 10px;\n \
                margin-top: 10px;\n \
            }\n \
            #base2 {\n \
                width : 1024px;\n \
                height: 1024px;\n \
                margin-left: 10x;\n \
                margin-top: 10px;\n \
                transform: translate(0px, 0px); \n \
            }\n \
            #base3 {\n \
                width : 1024px;\n \
                height: 1024px;\n \
                margin-left: 10px;\n \
                margin-top: 10px;\n \
                transform: translate(0px, 0px); \n \
            }\n \
        </style>\n \
    </head>\n \
    <body>\n "

START_DIV_1 = " \
        <svg id='base1'>\n "

START_DIV_2 = " \
        <svg id='base2'>\n "

START_DIV_3 = " \
        <svg id='base3'>\n "

END_DIV = " \
        </svg>\n "

END_FILE = "\
    </body>\n \
</html>\n "