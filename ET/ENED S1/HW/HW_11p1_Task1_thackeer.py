# Activity Python: Homework 11 Part 1 Task 1
# File: HW_11p1_Task1_thackeer.py
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
# Uses the speed of light, speed of a mobile, and mass of a mobile to output p, q, and Gam
c = float(input("Speed of Light: "))
v = float(input("Speed of the mobile: "))
m = float(input("Mass of the mobile: "))
G = abs((1/(1-(v/c)**2)**.5))
p = m*v
q = p*G
print("P:", "{:.2e}".format(p), "Q:", "{:.2e}".format(q), "Gam:", "{:.2f}".format(G))