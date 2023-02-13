# Assignment
# File:    HW_1p2_PythonFunctions
# Date:    1/19/23
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

SnowFall = open('Snow_Fall.txt','r')

Snow = SnowFall.readlines()
date=[]
fall=[]

for k in range(len(Snow)):
    Vals = Snow[k].split()
    date.append(Vals[0])
    fall.append(Vals[1])
    m = max(fall)

print('Maximum Snowfall: {0:.2f} inches on {1}'.format(m,date[fall.index(m)]))
  print(m)
  print(date[fall.index(m)])  
SnowFall.close()