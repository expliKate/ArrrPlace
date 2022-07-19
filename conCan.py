"""
This is an object that represents the canvas.

"ConCan" stands for "Conceptual Canvas".
"""

import matplotlib

width = 1
height = 1
maybeADict = {}
#pixels = [[0 for x in range(width)] for y in range(height)]     # This feels wrong, but it doesn't work if it's not initialized.

""" Returns a given hex color as RGB. """
def rgbConverter(hexColor):
    rgb_color_float = matplotlib.colors.to_rgb(hexColor)
    r = int(rgb_color_float[0] * 255)
    g = int(rgb_color_float[1] * 255)
    b = int(rgb_color_float[2] * 255)
    return (r, g, b)
    # TODO: Use ceiling and floor functions to avoid errors with using this new tuple.

""" Returns a given RGB color as a hex color.
    Does not currently work. Hard-coded to return black.
    Not currently used or needed.
 """
def hexConverter(rgbColor):
    # TODO: Actually calculate hex from RGB.
    return "#000000"

class conCan():

    # TODO: In Python, should you always have a constructor for no data provided? Are they called constructors in Python?
    def __init__(self,width_in,height_in):
        global width
        global height
        global pixels

        width, height = width_in, height_in
        
        #TODO: When I was using a 2D array, I left my self this note here: Use comprehensions. Replace this logic elsewhere with comprehensions; need to search.
        for x in range(width):
            for y in range(height):
                maybeADict[x,y] = rgbConverter("#FFFFFF")

        super().__init__()

    def updatePixel(self,x,y,color):
        while True:
            try:
                maybeADict[x,y] = rgbConverter(color)
                break
            except IndexError:
                break



    def getWidth():
        return width

    def getHeight():
        return height

    """ Return's the color of the pixel at the current location in RGB.
    """
    def getColorRGB(x,y):
        return maybeADict[x,y]

    """ Returns pixel's color in hexadecimal notation.
        Not currently used or needed. """
    def getColorHex(x,y):
        return hexConverter([maybeADict[x,y]])


    # TODO: Make a batch-update function