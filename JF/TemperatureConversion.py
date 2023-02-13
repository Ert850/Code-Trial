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

TempC = open('TempC.txt','r')
TempF = open('TempF.txt','w')

Temp = TempC.readlines()

for k in range(len(Temp)):
    Degree = float(Temp[k])
    F = Degree*(9/5)+32
    TempF.write('{0:.2f} F\n'.format(F))

TempC.close()
TempF.close()