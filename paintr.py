"""
This draws a colored square on a small window.

Modified from ZetCode PyQt5 tutorial by Jan Bodnar
Website: zetcode.com
"""

from curses import color_content
from matplotlib import colors
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
from conCan import conCan

class paintr(QWidget):
#class paintr(x_coord,y_coord,color):   # This isn't how you do this. For objects, the function __init__ gets called using the class name.
    cc = ""

    x_coord = 0
    y_coord = 0
    color = (0,0,0)
    qp = ""

    #app = QApplication(sys.argv)
    
    # [from online: should not have a global reference to a widget] OK, I think I need a global structure of my own creation which
    # is just TheCanvas, size user-defined, contents updatable but will preserve existing contents for each pixel if no update made.
    # So what SHOULD be on TheCanvas is determined programmatically (in Main.py). Actually putting it there is what this class should
    # do. So there could be a method here, "UpdateCanvas", that takes data from Main.py, updates the data structure - the conceptual 
    # canvas - and then redraws the pixels. (Probably we want a list of updated pixels so we are only drawing pixels that were actually
    # updated.) Possible risk here that the new data structure abstracts too much.


    # TODO: Still need to test if my new "WrapErUp" is a good solution. In other words, I'm in the process of fully deprecating main() in
    # this class.

    def __init__(self,cc_in):
        cc = cc_in

        super().__init__()
        self.initUI()

    def initUI(self):
        global app
        global qp

        qp = QPainter()
        qp.begin(self)
        app = QApplication(sys.argv)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Oh, Canada.")
        self.show()

    def drawPixels(event, qp):
        global cc
        global x_coord
        global y_coord
        global color

        for i in range(cc.getWidth()):
            for j in range(cc.getHeight()):
                x_coord = i
                y_coord = j
                qp.setPen(QColor(cc.getColorRGB(i,j)))
                qp.drawPoint(i,j)

    def paintEvent(self,event):
        print("Paint event begins.")
        global x_coord
        global y_coord
        global color
        global qp

        #self.drawPixels(event, qp)
        self.drawPixels(event, qp)
        qp.end()    

    def updatePixel(x_coord_in, y_coord_in, color_in):
        global x_coord
        global y_coord
        global color

        x_coord = x_coord_in
        y_coord = y_coord_in
        color = color_in
        #self.repaint()

""" 
# TODO: It should be possible to remove these.
def main(x_coord,y_coord,color):
    # print("This should never get called.")
    app = QApplication(sys.argv)
    ex = paintr(x_coord,y_coord,color)

if __name__ == '__main__':
    # print("This should also never get called.")
    main("","","") """