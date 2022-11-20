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
# Take Pressure and Temperature inputs and output corresponding phase state of water, or errors of inputs
from cmath import log, exp
P = input("Pressure (atm): ")
T = input("Temperature (Celsius): ")
try:
    int(P or T) and int(P and T)
    C = 0
except ValueError:
    try:
        float(P or T) and float(P and T)
        C = 0
    except ValueError:
        C = 1
if C == 1:
    print("Invalid Input - Not Number")
else:
    P = float(P)
    T = float(T)
    if P < 0:
        print("Invalid Input - Negative Pressure")
    else:
        T = T + 273.15
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