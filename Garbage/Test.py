from cgi import test
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


global myStr

def window():
    global myStr
    
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    canvasUpdater()
    b.setText(myStr)
    w.setGeometry(100,100,900,60)
    b.move(50,20)
    w.setWindowTitle("Not Proud of This, TBH")
    w.show()
    sys.exit(app.exec_())

def canvasUpdater():
    global myStr
    myStr = "There's someone else that you're supposed to be; something deep inside of you that still wants out, and shame on you if you don't set it free."

if __name__ == '__main__':
   window()