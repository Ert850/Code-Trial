# Activity Python 1: Task 3
# File: Task3_thackeer.py 
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
# Computes the equivalent spring constant and total displacement as well as the force 
# and displacement for each spring for both parallel and series configurations
K1 = float(input("Enter a K1 Value: "))
K2 = float(input("Enter a K2 Value: "))
FTotal = float(input("Enter a FTotal Value: "))
Type = (input("Enter a type of configuration(S for Series or P for Parallel) Value: "))
if 0 <= K1 and 0 <= K2 and 0 <= FTotal:
    if Type == "S":
        PreKeq = (1/K1) + (1/K2)
        Keq = 1/PreKeq
        F1 = FTotal
        F2 = F1
        XTotal = FTotal / Keq
        X1 = F1 / K1
        X2 = F2 / K2
        print("Keq:", Keq)
        print("F1:", F1)
        print("F2:", F2)
        print("X1:", X1)
        print("X2:", X2)
        print("XTotal:", XTotal)
    elif Type == "P":
        Keq = K1 + K2
        XTotal = FTotal / Keq
        X1 = XTotal
        X2 = X1
        F1 = K1 * XTotal
        F2 = K2 * XTotal
        print("Keq:", Keq)
        print("F1:", F1)
        print("F2:", F2)
        print("X1:", X1)
        print("X2:", X2)
        print("XTotal:", XTotal)
    else:
        print("Invalid Configuration Input")
else:
    print("Invalid Input Values")