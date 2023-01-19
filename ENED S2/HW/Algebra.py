# Activity Python: Algebra
# File: Algebra.py 
# Date:    18 January 2023
# By:      Elijah Thacker
# Section: 006
# Team:    063
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
# Function defined for solving algebraic functions
def Algebra(a1,b1,c1,a2,b2,c2):
    T = a1*b2-a2*b1
    if T == 0:
        x = "No unique solution"
        y = "No unique solution"
    else:
        x = "{:0.3f}".format((c2-(b2*c1)/(b1))/(a2-(b2*a1)/(b1)))
        y = "{:0.3f}".format((c1-(a1*x))/(b1))
    return x,y