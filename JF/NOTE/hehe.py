# Assignment
# File: 
# Date:    12/7/22
# By:      Jacob Freidline
# Section: 005
# Team:    259
# 
# ELECTRONIC SIGNATURE
# Jacob Freidline
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for 
# all your python files the rest of the semester.

def Algebra(a1,b1,c1,a2,b2,c2):
    T = a1*b2-a2*b1
    if T == 0:
        x = "No unique solution"
        y = "No unique solution"
    else:
        x = "{:0.3f}".format((c2-(b2*c1)/(b1))/(a2-(b2*a1)/(b1)))
        y = "{:0.3f}".format((c1-(a1*x))/(b1))
    return x,y