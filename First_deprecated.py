import os
import tkinter
import time
import pandas as pd
import numpy as np

# TODO: Is this the right case for function names?
def MakeCanvasDataStructure():
    #Define finished data structure
    #Get data from file
    return 0

def DisplayCanvasHistory():
    return 0

def DisplaySliderCanvas():
    return 0

# thisFileName = "Files\2022_place_canvas_history-000000000000.csv"
thisFileName = "2022_place_canvas_history-000000000000.csv"
# TODO: access file in subdirectory instead of this messy workaround.

# TODO: Once you can display the Canvas, find these correct numbers
""" Canada's final location (best guess):
175, 450
244, 528 """
# Set pleasing variable names for these numbers
xmin = 175
xmax = 244
ymin = 450
ymax = 528

# This is to help me keep line width standard; not currently using this
#02345678911234567892123456789312345678941234567895123456789612345678961234567897123456789

""" with open(thisFileName) as workingFile:
    print(workingFile.readline())
    print(workingFile.readline()) """

# print("File closed successfully? " + str(workingFile.closed))

# # TODO: Add two columns containing the split x/y coords?
# pixelHx = pd.read_csv(thisFileName)
# # pixelHx"["x_coord"] = pixel["coordinate"]
# print(pixelHx["coordinate"].head())
# # print(pixelHx)
# # print(pixelHx[["timestamp", "pixel_color", "coordinate"]])
# # print(pixelHx[["timestamp", "pixel_color", "coordinate"]])
# # print(pixelHx[["coordinate"]])
# # (x_coord >= xmin) & (x_coord <= xmax) & (y_coord >=ymin) & (y_coord <= ymax)

# TODO: Use reddit data to update pixels 
# TODO: Create list of all (relevant) pixels and their color that will get updated for every tick (or ???)
# TODO: (Manually) determine the max size of the full Canadian canvas (flag moved around, got duplicated, etc)

window = tkinter.Tk()
#window.mainloop() #This doesn't work.
label = tkinter.Label(window, text="dis mine") # Create a text label
# label.pack(padx=20, pady=20) # Pack it into the window
label.pack() # Pack it into the window
#window.update() # This ooesn't work.
window.mainloop()

# TODO: Modify colored pixels instead of labels
# TODO: Enable re-sizing. (Related: May want default image to be larger than 1 pixel per pixel.)

# print("My file is: " + thisFileName)