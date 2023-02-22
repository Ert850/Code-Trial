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
# this program will calculate the equivalent resistance specified
# by the user

# import libraries
import math
import ResistorCombos

# get values from the user
r1 = float(input('Please enter R1: '))
r2 = float(input('Please enter R2: '))
C = input('Please enter the connection type (s = series, p = parallel)')

# determine the equivalent resistance
if C == 's' or C == 'S':
    Rtotal = ResistorCombos.Rseries(r1,r2)
    print('Series combination: {0:0.2f}'.format(Rtotal))
elif C == 'p' or C == 'P':
    Rtotal = ResistorCombos.Rparallel(r1,r2)
    print('Parallel combination: {0:0.2f}'.format(Rtotal))
else:
    print('That input is not a valid connection type')