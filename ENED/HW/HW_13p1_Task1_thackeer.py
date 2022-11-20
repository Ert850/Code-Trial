# Activity Python: Homework 13 Part 1 Task 1
# File: HW_13p1_Task1_thackeer.py 
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
# Takes Pressure and Temperature inputs and outputs corresponding phase state of water, or errors of inputs, and loops
from cmath import log, exp
R = "Y"
while R == "Y":
    P = input("Pressure (atm): ")
    T = input("Temperature (Celsius): ")
    try:
        int(P or T) and int(P and T) and float(P or T) and float(P and T)
        C = "Y"
    except ValueError:
        print("Invalid Input - Not Number")
        C = "N"
    if C == "Y":
        P = float(P)
        T = float(T)+273.15
        if P < 0:
            print("Invalid Input - Negative Pressure")
        else:
            P1 = abs(0.006*exp(6293*((1/273.15)-(1/T))-0.56*log(T/273.15)))
            P2 = abs(0.006*exp(6808*((1/273.15)-(1/T))-5.09*log(T/273.15)))
            if T > 647 and P > 218:
                print("Super Critical Liquid")
            elif T < 273.15:
                if P > P1:
                    print("Solid")
                else:
                    print("Gas")
            elif P > P2:
                print("Liquid")
            else:
                print("Gas")
    R = input("Run again? (Y or N): ")
    if R == "y":
        R = "Y"
    elif R == "Y":
        R = "Y"
    elif R == "n":
        quit()
    elif R == "N":
        quit()
    else:
        R = 1
        while R == 1:
            R = input("Invalid Entry - Run again? (Y or N): ")
            if R == "y":
                R = "Y"
            elif R == "Y":
                R = "Y"
            elif R == "n":
                quit()
            elif R == "N":
                quit()
            else:
                R = 1