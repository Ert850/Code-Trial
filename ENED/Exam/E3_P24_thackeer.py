# Activity Python: Exam 3 Part 24
# File: E3_P24_thackeer.py
# Date:    28 November 2022
# By:      Elijah Thacker
# Section: 006
# Team:    088
# 
# ELECTRONIC SIGNATURE
# Elijah Thacker
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# Develop a python script to allow a user to define a line model type, 
# and then proceed to enter points and recieve the equation for those points

import math
# Allows user to specify a model type 
type = input("Enter a Model Type ('L' for linear, 'P' for power, or 'E' for exponential): ")
# Checks if the user imputted a valid value
if type == 'L' or type == 'P' or type == 'E':
    # Allows user to imput coordinates of two points, one at a time
    x1 = float(input("Enter X1: "))
    y1 = float(input("Enter Y1: "))
    x2 = float(input("Enter X2: "))
    y2 = float(input("Enter X2: "))
    # If the user specified the equation was linear, then the program calculates the slope and y-intercept for that model
    if type == 'L':
        slope = (y2 - y1) / (x2 - x1)
        yint = y1 - (slope * x1)
        # Outputs linear equation
        print("Linear Equation: y =", "{0:.4f}".format(slope), "x +", "{0:.4f}".format(yint))
    # If the user specified the equation was power, then the program calculates the slope and y-intercept for that model
    elif type == 'P':
        slope = (math.log10(y2) - math.log(y1)) / (math.log10(x2) - math.log10(x1))
        yint = 10 ** (math.log10(y1) - (slope * math.log10(x1)))
        # Outputs power equation
        print("Power Equation: y =", "{0:.4f}".format(slope), "x +", "{0:.4f}".format(yint))
    # If the user specified the equation was exponential, then the program calculates the slope and y-intercept for that model
    elif type == 'E':
        slope = (math.log(y2) - math.log(y1)) / (x2 - x1)
        yint = math.exp(math.log(y1) - (slope * x1))
        # Outputs exponential equation
        print("Exponential Equation: y =", "{0:.4f}".format(slope), "x +", "{0:.4f}".format(yint))
# Catch all in the case of error in inputted value
else:
    # Informs the user that the value inputed for the model type was invalid
    print("The Model Type is Invalid (try 'L', 'P', or 'E')")
