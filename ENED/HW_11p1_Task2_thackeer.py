# Activity Python: Homwork 11 Part 1 Task 2
# File: HW_11p1_Task2_thackeer.py 
# Date:    17 November 2022
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
# Calculates Velocity from initial speed, mass, and constant K
Vo = float(input("Enter the initial speed (Vo, m/s): "))
K = float(input("Enter the constant (K, Kg*m^2/s): "))
m = float(input("Enter the mass of the mobile (m, Kg): "))
V2 = Vo * 39.4
K2 = K * 15477.02
M2 = m * 0.07
V3 = V2**2
KM = K2/M2
V = (V3-KM)**.5
print("The Value of V =", "{:.2f}".format(V))