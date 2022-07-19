import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# For use while I'm trying to find the limits of Canadian flag art
# You might need different buffers for each axis.
buffer = 100

""" Canada's final location (best guess):
175, 450
244, 528 """
# Set pleasing variable names for these numbers
xmin = 175
xmax = 244
ymin = 450
ymax = 528

app = QApplication(sys.argv)    # Can use "[]" instead of "argv" if you're sure you won't be getting args from whoever calls the script.

myWin = QWidget()
myWin.setWindowTitle('Eventually Canada')
myWin.setGeometry(100, 100, (xmax-xmin) + buffer, (ymax-ymin) + buffer)
#myWin.setGeometry(100,100,560,320) # This is more appealing to look at.
myWin.move(60, 15)  # I don't understand what this is.
myWin.show()
#myMsg = QLabel('<h1>There will be some Canada here.</h1>', parent=myWin)
#myMsg.move(60, 15)
pal = myWin.palette()
pal.setColor(myWin.backgroundRole(), Qt.white)
myWin.setPalette(pal)

qp = QPainter(self)
qp.begin(myWin)
qp.setPen(Qt.black)
#size = myWin.size()
qp.drawPoint(3,4)
qp.drawPoint(3,5)
qp.drawPoint(4,4)
qp.drawPoint(4,5)

qp.end()

sys.exit(app.exec_())

# When you finally need it, the calculation is going to be:
# x = thisX - xmin
# y = thisY - ymin
# While finding the image limits, it will be:
# x = thisX - xmin + (buffer/2)
# y = thisY - ymin + (buffer/2)