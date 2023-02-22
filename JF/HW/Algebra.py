# Assignment
# File:    HW_1p2_PythonFunctions
# Date:    1/19/23
# By:      Jacob Freidline
# Section: 005
# Team:    72
# 
# ELECTRONIC SIGNATURE
# Jacob Freidline
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# Function that calculates and outputs values for x and y
# given two different linear equations and the inputs a1,b1,c1,a2,b2,c2

def Algebra(a1,b1,c1,a2,b2,c2):
    s = a1*b2-a2*b1
    if s == 0:
        print('There is no unique solution for x and y')
    else:
        x = "{:0.3f}".format((c2-(b2*c1)/(b1))/(a2-(b2*a1)/(b1)))
        y = "{:0.3f}".format((c1-(a1*x))/(b1))
    return x,y
