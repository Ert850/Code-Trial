# Assignment
# File:    E4_P19_freidljs
# Date:    2/13/23
# By:      Jacob Freidline
# Section: 005
# Team:    72
# 
# ELECTRONIC SIGNATURE
# Jacob Freidline
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for 
# all your python files the rest of the semester.

import math

Vo = int(input('Enter the initial velocity (m/s): '))
N = int(input('Enter the number of angles: '))

for k in range(N):
    angleD = int(input('Enter the angle (in degrees): '))
    while angleD <= 0 or angleD >=90:
        angleD = int(input('Enter the angle (in degrees): '))
    angleA = angleD*math.pi/180
    maxH = ((Vo**2)*(math.sin(angleA)**2))/19.62
    maxR = (2(Vo**2)*(math.cos(angleA))*(math.sin(angleA)))/9.81

print('Velocity: {0}\n'.format(Vo))
print('Launch Angle: {0}\n'.format(angleD))
print('Maximum Height: {0:.1f}\n'.format(maxH))
print('Maximum Range: {0:.1f}'.format(maxR))