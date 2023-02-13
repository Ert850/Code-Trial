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
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for 
# all your python files the rest of the semester.

import Alloys

AllNum = int(input('Enter an Alloy Number (2024, 7075, 356): '))
while AllNum != 2024 and AllNum != 7075 and AllNum != 356:
    AllNum = int(input('Enter an Alloy Number (2024, 7075, 356): '))
Numlbs = int(input('Enter required number of pounds: '))
while Numlbs <= 0:
    int(input('Enter required number of pounds: '))

Cost = Alloys.Alloys(AllNum,Numlbs)
print('{:0.2f}'.format(Cost))