""" Replays a given portion of the 2022 /r/place canvas.
    For now, it will only display one pixel change per tenth of a second, even though
    the dataset contains changes every thousandth of a second.
"""

import os
import time
import pandas as pd
import numpy as np
from paintr import paintr
from conCan import conCan

# TODO: Improve error handling ("fail gracefully")
# TODO: Should I be using more methods (difference between methods and functions?)?

x_coord = 0
y_coord  = 0
myp = 0

# TODO: Is this the right case for function names?
# TODO: Actually, just general PEP8 stuff
def MakeCanvasDataStructure():
    #Define finished data structure
    #Get data from file
    return 0

def DisplayCanvasHistory():
    return 0

def DisplaySliderCanvas():
    return 0

def splitCoords(coordString):
    temp = str(coordString).split(",") # TODO: Better to check that this really did produce a list of exactly 2 items
    x_coord = temp[0]
    y_coord = temp[1]
    return (int(x_coord),int(y_coord))

# thisFileName = "Files\2022_place_canvas_history-000000000000.csv"
# TODO: look at all ?12? files, not just this example one
thisFileName = "2022_place_canvas_history-000000000000.csv"
# TODO: access file in subdirectory instead of this messy workaround.

# TODO: Once you can display the Canvas, find these correct numbers
""" Canada's final location (best guess):
175, 450
244, 528 """
# Set pleasing variable names for these numbers
x_min = 175
x_max = 244
y_min = 450
y_max = 528

pixelHx = pd.read_csv(thisFileName)

# This [1] is real hack-y:
pixelHx["x_coord"] = splitCoords(pixelHx["coordinate"][1])[0]
pixelHx["y_coord"] = splitCoords(pixelHx["coordinate"][1])[1]
#I got this by just playing around with variables in debug until I found one that ran the function on only the coordinate column.

# This is a bunch of stuff I used to explore the new DataFrame.
# print("Some facts about pixelHx:\n")
# print("Length: " + str(len(pixelHx)))
# print("Columns: " + str(pixelHx.columns))
#print("1st pixel coordinate + color: " + pixelHx['coordinate','pixel_color'][0])
#print("1st pixel coordinate + color: " + pixelHx['coordinate'][0] + "|" + pixelHx['pixel_color'][0])
#temp2 = pixelHx[["coordinate","pixel_color"]]
#print(str(temp2.head()))
# print("New thing: " + pixelHx[0:2,3])
# temp = splitCoords(pixelHx['coordinate'][0])
# print("Coords as a tuple: " + str(temp))
# print("Same Coords, but adjusted: " + str(temp[0] - xmin) + "~" + str(temp[1] - ymin))
# print("2nd pixel coordinate + color: " + pixelHx['coordinate'][1] + "|" + pixelHx['pixel_color'][1])
# print("3rd pixel color + coordinate: " + pixelHx['coordinate'][2] + "|" + pixelHx['pixel_color'][2])
# print("4th pixel color + coordinate: " + pixelHx['coordinate'][3] + "|" + pixelHx['pixel_color'][3])
# # pixelHx"["x_coord"] = pixel["coordinate"]
#print(pixelHx["coordinate"].head())
#print(pixelHx["pixel_color"][1]) # This syntax seems to be giving me the string value for pixel_color in the second row.
#print(pixelHx.columns)

#pixelHx = pixelHx.loc[pixelHx["coordinate"].str.split(pat=",") <= 9]

#print(pixelHx["coordinate"].head())
#print(pixelHx.head())
pd.set_option('display.max_colwidth', None) #I don't understand why the display won't show color. It appears to be about the length of each row, but this isn't helping.
print(pixelHx)

#otherVar = pixelHx['pixel_color'][0]
#temp2 = "temp"
#temp2 = pixelHx[0]
# cc = conCan(10,10)
cc = conCan((x_max - x_min + 1), (y_max - y_min + 1))
# TODO: Adjust coords before adding them to conceptual canvas so they are treat the minimum corner as 0,0 instead of (x_min,y_min).
""" cc.updatePixel(2,3,(pixelHx[0]['pixel_color']))
cc.updatePixel(3,4,(pixelHx['pixel_color'][1]))
cc.updatePixel(4,5,(pixelHx['pixel_color'][2]))
cc.updatePixel(5,6,(pixelHx['pixel_color'][3]))
cc.updatePixel(6,7,(pixelHx['pixel_color'][4]))
cc.updatePixel(7,8,(pixelHx['pixel_color'][5]))
cc.updatePixel(8,9,(pixelHx['pixel_color'][6])) """

#This is going to do a bunch of pointless updating and then display just the final configuration. This is just for testing during development.
# TODO: Yeah, this is slow as Hell. Might need to look into threading to make this feasible. Or just go straight to video.
for ind in pixelHx.index:
    if pixelHx['x_coord'][ind] >= x_min and pixelHx['x_coord'][ind] <= x_max and pixelHx['y_coord'][ind] >= y_min and pixelHx['y_coord'][ind] <= y_max:
        cc.updatePixel(pixelHx['x_coord'][ind] - x_min + 1,pixelHx['y_coord'][ind] - y_min + 1,str(pixelHx['pixel_color'][ind]))

# TODO: Use reddit data to update pixels 
# TODO: Create list of all (relevant) pixels and their color that will get updated for every tick (or ???)
# TODO: (Manually) determine the max size of the
#  full Canadian canvas (flag moved around, got duplicated, etc)
# First do it without a loop
myP = paintr(cc)
#paintr.main(1,2,pixelHx["pixel_color"][0])
# paintr.updatePixel(2,2,pixelHx["pixel_color"][1])
# paintr.updatePixel(3,2,pixelHx["pixel_color"][2])
# paintr.updatePixel(4,2,pixelHx["pixel_color"][3])

# TODO: Modify colored pixels instead of labels
# TODO: Enable re-sizing. (Related: May want default image to be larger than 1 pixel per pixel.)