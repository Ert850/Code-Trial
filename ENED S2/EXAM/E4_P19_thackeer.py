# Activity Python: Exam 4 Part 19
# File: E4_P19_thackeer.py 
# Date:    13 February 2023
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
# Use input values to calculate projectile motion variables
import math
def Rocket(Vo,N):
    angle = 180
    while angle < 0 or angle > 90 or angle == 0 or angle == 90:
        angle = input("Angle (degrees between ): ")
    height = (Vo^2 * math.sin(angle*math.pi/180))/2*9.81
    range = (2*(Vo^2)*math.cos(angle*math.pi/180)*math.sin(angle*math.pi/180))/9.81
    print("Vo=","{:0.1f}".format(Vo),"m/s, Th=", "{:0.1f}".format(angle),"deg., MaxHeight=","{:0.1f}".format(height),"m, MaxRange=", "{:0.1f}".format(range),"m")