# Assignment
# File:    Stats
# Date:    1/26/23
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

import math

def Stats(list):
    avg = 0
    var = 0

    for k in range(len(list)):
        AvgVal = list[k]+AvgVal 
    mean = AvgVal/(len(list))

    for k in range(len(list)):
        VarVal = (list[k]-mean)**2+var
    sd = math.sqrt(var/len(list)-1)

    return mean,sd