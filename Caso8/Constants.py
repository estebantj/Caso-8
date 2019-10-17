IMAGES = ["firstImage.jpg", "secondImage.jpg", "thirdImage.jpg", "fourthImage.png", "beach.png", "guacamaya.png"]
NUMBER_OF_LINES = 9
NUMBER_OF_SECTORS = (NUMBER_OF_LINES + 1) * (NUMBER_OF_LINES + 1)
NUMBERS_OF_SAMPLES_PER_SECTOR = 200
PERCENTAGE_FOR_SAMPLES = 50
PERCENTAGE_PER_ITERATION = 10
AMOUNT_OF_BITS = 11
NUMBER_OF_GENERATIONS = 15
NUMBER_OF_CHILDREN_PER_GENERATION = 50
IMAGESIZE = 0
HTMLFILE = None
HTML1 = " \
<html>\n \
    <head>\n \
        <style>\n \
            #base {\n \
                width : 1024px;\n \
                height: 1024px;\n \
                margin-left: 10px;\n \
                margin-top: 10px;\n \
            }\n \
        </style>\n \
    </head>\n \
    <body>\n \
        <svg id='base'>\n "
HTML2 = " \
        </svg>\n \
    </body>\n \
</html>\n "
