# Activity Python: Homwork 11 Part 1 Task 3
# File: HW_11p1_Task3_thackeer.py 
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
# Uses incident wave amplitude, intrinsic impedences, incident wave angle, and 
# transmitted wave angle to compute amplitude of the reflected and transmitted wave
from cmath import cos, pi
ai = float(input("Enter the amplitude of the incident wave: "))
n1 = float(input("Enter the intrinsic impedence of medium 1: "))
n2 = float(input("Enter the intrinsic impedence of medium 2: "))
di = float(input("Enter the angle of the incident wave (in Degrees): "))*pi/180
dt = float(input("Enter the angle of the transmitted wave (in Degrees): "))*pi/180
at = abs(ai*((2*n2*cos(di))/(n2*cos(dt)+n1*cos(di))))
ar = abs(ai*((n2*cos(di)-n1*cos(dt))/(n2*cos(di)+n1*cos(dt))))
print("The amplitude of the transmitted wave is E_t =", "{:0.2f}".format(at), "V/m")
print("The amplitude of the reflected wave is E_t =", "{:0.2f}".format(ar), "V/m")