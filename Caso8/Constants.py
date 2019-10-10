IMAGES = ["firstImage.jpg", "secondImage.jpg", "thirdImage.jpg"]
NUMBER_OF_LINES = 3
NUMBER_OF_SECTORS = (NUMBER_OF_LINES + 1) * (NUMBER_OF_LINES + 1)
NUMBERS_OF_SAMPLES_PER_SECTOR = 200
PERCENTAGE_FOR_SAMPLES = 25
PERCENTAGE_PER_ITERATION = 5
IMAGESIZE = 0
HTMLFILE = None
HTML1 = " \
<html>\n \
    <head>\n \
        <style>\n \
            #base {\n \
                width : 1024px;\n \
                height: 1024px;\n \
                margin-left: 300px;\n \
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