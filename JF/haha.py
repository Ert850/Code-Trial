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

def CostCalc(AlloyNum,Count):
    if AlloyNum == 356:
        Cost = Count * 1.36697
    elif AlloyNum == 2048:
        Cost = Count * 1.28049
    elif AlloyNum == 7075:
        Cost = Count * 1.24355
    return Cost