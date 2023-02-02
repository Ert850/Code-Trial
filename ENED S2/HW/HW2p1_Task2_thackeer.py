# Activity Python: HW 2 Part 1 Task 2
# File: HW2p1_Task2_thackeer.py 
# Date:    26 January 2023
# By:      Elijah Thacker
# Section: 005
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
# Sorter of substances with max and min temps
import math

Sub = input('Enter Substance (Methanol, Butane, Octane): ')
while Sub != 'Methanol' and Sub != 'Butane' and Sub != 'Octane':
    Sub = input('Incorrect. Enter Substance (Methanol, Butane, Octane): ')
A = 0
B = 0
C = 0
TMin = 0
TMax = 0
if Sub == 'Methanol':
    A = 8.0724
    B = 1574.99
    C = 238.73
    TMin = -16
    TMax = 91
elif Sub == 'Butane':
    A = 6.80896
    B = 935.86
    C = 238.73
    TMin = -78
    TMax = 19
elif Sub == 'Octane':
    A = 6.9094
    B = 1349.82
    C = 209.385
    TMin = 19
    TMax = 152
DTemp = (TMax-TMin)/19
Temp = []
for k in range(20):
    T = TMin+k*DTemp
    Temp.append(T)
for k in range(len(Temp)):
    P = 10**(A-(B/(C+Temp[k])))
    print(f'Temperature: {Temp[k]:.3f} (C); Presssure: {P:.3f} (mmHG)')