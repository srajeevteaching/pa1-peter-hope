# Team Members: Peter Hope
# Course: CS151, Dr.Rajeev
# Date: 9/22/21
# Programming Assignment: 1
# Program Inputs: length, width, and height of the room
# Program Outputs: Total area to be painted, gallons of primer needed, gallons of paint needed
print ("This Program will calculate the area that needs to be painted in a room and how much primer and paint will be needed to do it!")

# import math module

import math

# ask for inputs of length, width, and height
print ("Please input the dimensions of the room in feet!")
lengthStr = input("Length: ")
widthStr = input("Width: ")
heightStr = input("Height: ")
#convert strings to floats
length = float (lengthStr)
width = float (widthStr)
height = float (heightStr)
# calculate the total area to be painted
totalArea = (length*width)+(length*height*2)+(width*height*2)
# calculate gallons of primer needed
primerGal = totalArea/200
# calculate gallons of paint needed
paintGal = totalArea/350
# print all outputs
print "The total area to be painted is:", totalArea, "square feet"
print "The number of gallons of primer needed is:", primerGal, "gallons"
print "The number of gallons of paint needed is:", paintGal, "gallons"
