# Activity Python 1: Task 2
# File: Task2_thackeer.py 
# Date:    14 November 2022
# By:      Elijah Thacker
# Section: 006
# Team:    088
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
# Uses pH of a solution to tell if a solution is Acidic, Neutral, Basic, or Invalid
pH = float(input("Enter the pH of the solution: "))
if 0 <= pH <= 14:
    if 0 <= pH <= 7:
        print("Acidic")
    elif pH == 7:
        print("Neutral")
    else:
        print("Basic")
else:
    print("Invalid")