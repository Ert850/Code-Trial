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
# Function that calculates the total cost of different aluminum
# alloys based on which alloy type it is and the number of pounds
# of the specified alloy

def Alloys(allnum,numlbs):
    if allnum == 2024:
        cost = numlbs*1.28049
    elif allnum == 7075:
        cost = numlbs*1.24355
    elif allnum == 356:
        cost = numlbs*1.36697
    return cost