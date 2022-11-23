# Activity Python: Homework 13 Part 1 Task 2
# File: HW_13p1_Task2_thackeer.py 
# Date:    20 November 2022
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
# Takes metal name and crystal structure to calculate density and verify crystal choice with warnings
R = "Y"
while R == "Y":
    M = input("Metal (Al, Co, Cr): ")
    C = input("Crystal Stucture (FCC, BCC, HCP): ")
    Check1 = 0
    Check2 = 0
    try:
        int(M or C) and int(M and C) and float(M or C) and float(M and C)
        print("Invalid Input - Not Letters")
        Check = 0
    except ValueError:
        if M == "Al" or M == "Co" or M == "Cr":
            Check1 = 1
        else:
            print("Metal Invalid")
        if C == "FCC" or C == "BCC" or C == "HCP":
            Check2 = 1
        else:
            print("Crystal Structure Invalid")
    if Check1 + Check2 == 2:
        if M == "Al":
            MM = 26.98
            R = 0.1431
            D = 2.7
        elif M == "Co":
            MM = 58.93
            R = 0.1253
            D = 8.9
        else:
            MM = 52
            R = 0.1249
            D = 7.2
        if C == "FCC":
            A = (4*R)/(2**0.5)
            V = A**3
            NA = 4
        elif C == "BCC":
            A = (4*R)/(3**0.5)
            V = A**3
            NA = 2
        else:
            A = 2*R
            C = 1.63*A
            V = (3*(3**0.5)*C*(A**0.5))/2
            NA = 6
        print(A, C, V, NA)
        
        
         
    R = input("Run again? (Y or N): ")
    if R == "n" or R == "N":
        quit()
    elif R == "Y" or R == "y":
        R = "Y"
    else:
        R = 1
        while R == 1:
            R = input("Invalid Entry - Run again? (Y or N): ")
            if R == "n" or R == "N":
                quit()
            elif R == "Y" or R == "y":
                R = "Y"
            else:
                R = 1