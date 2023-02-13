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

# import libraries
import math

# defining the series calculation function
def Rseries(R1,R2):
    Req = R1+R2
    return Req

# defining the parallel calculation function
def Rparallel(R1,R2):
    a = R1*R2
    b = R1+R2
    Req = a/b
    return Req