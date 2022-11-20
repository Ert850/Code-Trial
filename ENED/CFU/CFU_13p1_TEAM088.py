# Activity Python 1: CFU_13p1_TEAM088
# File: CFU_13p1_TEAM088.py 
# Date:    14 November 2022
# By:      Elijah Thacker
# Section: 006
# Team:    088
# 
# ELECTRONIC SIGNATURE
# Elijah Thacker (Brody Bleuter, Alex Becker, Josh Wachs)
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# States if the view of an orthographic sketch is valid or invalid based on the views given, and gives the corresponding dimensions for that view if valid
View = input("State an orthographic view (F for Front, T for Top, R for Right: ")
if View == "F" or "f":
    print("Your Corresponding Dimesnions are Height and Width")
elif View == "T" or "t":
    print("Your Corresponding Dimesnions are Width and Depth")
elif View == "R" or "r":
    print("Your Corresponding Dimesnions are Depth and Height")
else:
    print("Invalid View Chosen")