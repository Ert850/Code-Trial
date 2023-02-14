# Assignment
# File:    E4_P20_freidljs
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

Data = open('Robot.txt','r')
Results = open('E4_freidljs.txt','w')
data = Data.readlines()

counterB = 0
counterX = 0
counterY = 0

for k in range(len(data)):
    Vals = data[k].split()
    x = Vals[0]
    y = Vals[1]
    if x >= 19.125 and x <= 19.5 and y >= 58 and y <= 59:
       counterB = counterB+1 
    else:  
        if x >= 19.125 and x <= 19.5:
            counterX = counterX+1
        if y >= 58 and y <= 59:
            counterY = counterY+1
    Xerror = x-19.3125
    Yerror = y-59
    Results.write('{0:.4f}\t{1:.4f}\n'.format(Xerror,Yerror))

print('Both x and y in acceptable range: {0}\n'.format(counterB))
print('x in acceptable range: {0}\n'.format(counterX))
print('y in acceptable range: {0}'.format(counterY))

Data.close()
Results.close()