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
# Prompts the user for a model type
type = input("Enter a Model Type ('L' for linear, 'P' for power, or 'E' for exponential): ")
# Checks if the user entered a valid model type
if type == 'L' or type == 'P' or type == 'E':
    # Prompts the user for the x and y coordinates of two data points
    x1 = float(input("Enter X1: "))
    y1 = float(input("Enter Y1: "))
    x2 = float(input("Enter X2: "))
    y2 = float(input("Enter X2: "))
    # If linear, then the program computes the equation for linear
    if type == 'L':
        slope = (y2 - y1) / (x2 - x1)
        yint = y1 - (slope * x1)
        # Outputs linear equation
        print("Linear Equation: y =", "{0:.4f}".format(slope), "x +", "{0:.4f}".format(yint))
    # If power, then the program computes the equation for power
    elif type == 'P':
        slope = (math.log10(y2) - math.log(y1)) / (math.log10(x2) - math.log10(x1))
        yint = 10 ** (math.log10(y1) - (slope * math.log10(x1)))
        # Outputs power equation
        print("Power Equation: y =", "{0:.4f}".format(yint), "x^", "{0:.4f}".format(slope))
    # If exponential, then the program computes the equation for exponential
    elif type == 'E':
        slope = (math.log(y2) - math.log(y1)) / (x2 - x1)
        yint = math.exp(math.log(y1) - (slope * x1))
        # Outputs exponential equation
        print("Exponential Equation: y =", "{0:.4f}".format(yint), "e^", "{0:.4f}".format(slope), "x")
# Runs in the case of an invalid model type
else:
    # Prints a message that the model type is invalid, and the program simply ends
    print("The Model Type is Invalid (try 'L', 'P', or 'E')")
