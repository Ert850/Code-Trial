# Activity Python 1: CFU 11.1: Python Sequential
# File: CFU_11p1_thackeer.py 
# Date:    31 October 2022
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
# Script designed to output Velocity of a Projectile given Range, Gravity, and Angle
# This script is a header template that will be used for 
# all your python files the rest of the semester.
import cmath
import math
G = float(input("Gravity (m/s): "))
Ab = float(input("Angle (degrees): "))
A = float(math.radians(Ab))
R = float(input("Range (m): "))
V = cmath.sqrt((G*R)/(cmath.sin(A))**2)
print(V)