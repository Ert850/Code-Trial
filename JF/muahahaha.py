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

import Alloys

AlloyNum = float(input("Enter Alloy Type (356, 2048, or 7075): "))
while AlloyNum != 356 and AlloyNum != 2048 and AlloyNum != 7075:
    if AlloyNum != 356 and AlloyNum != 2048 and AlloyNum != 7075:
        AlloyNum = float(input("Enter Alloy Type (356, 2048, or 7075): "))
Count = float(input("Pounds: "))
while Count <= 0:
    if Count <= 0:
        Count = float(input("Pounds (Positive Number): "))
        
Cost = Alloys.Costcalc(AlloyNum,Count)
print("{:0.2f}".format(Cost))