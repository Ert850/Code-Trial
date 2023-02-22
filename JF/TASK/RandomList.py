# Assignment
# File: 
# Date:    12/7/22
# By:      Jacob Freidline
# Section: 005
# Team:    259
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

import random
x = [0]
N = int(input('Select the number of times two dice are rolled: '))
while N <= 0:
    print('Error: Insert a positive number')
    N = int(input('Select the number of times two dice are rolled: '))
for k in range(N):
    Dice1 = random.randint(1,6)
    Dice2 = random.randint(1,6)
    S = Dice1+Dice2
    x.append(S)
for k in range(N):
    num = x[k]
print
