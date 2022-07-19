"""
This is an object that represents one pixel.

Pixels have a location (an x and y coordinate) and a color. The color
can be changed. The location cannot.

Is this ridiculous? It just seems like it will be easier because there are specific
rules to pixels.

UPDATE: Yes, this is ridiculous. The array is already implicitly storing x and y for each pixel, so a collection of pixels is just
a collection of colors.
"""

from curses import can_change_color
import matplotlib

x_coord = 0
y_coord = 0
color = ""      # This is probably unnecessary.
rgbcolor = (0,0,0)

class myPixel():
    
    def __init__(self,x_coord_in,y_coord_in,color_in):
        global x_coord
        global y_coord

        x_coord = x_coord_in
        y_coord = y_coord_in
        self.changeColor(color_in)

        super().__init__()

    def changeColor(color_in):
        global color
        global rgbcolor

        color = color_in

        rgb_color_float = matplotlib.colors.to_rgb(color)
        r = int(rgb_color_float[0] * 255)
        g = int(rgb_color_float[1] * 255)
        b = int(rgb_color_float[2] * 255)
        rgb_color = (r, g, b)
        # TODO: Use ceiling and floor functions to avoid errors with using this new tuple.