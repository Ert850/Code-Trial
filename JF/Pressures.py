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

import math
import PressureCombos

n = float(input('Enter a numerical value for pressure: '))
pi = input('Enter the units for the pressure value entered (Pa or psi): ')
pf = input('Enter the desired units for the pressure value (Pa or psi): ')

if pi == 'Pa' and pf == 'psi':
    ptotal = PressureCombos.Patopsi(n)
    print('Pressure in psi: {0:0.8f}'.format(ptotal))
elif pi == 'psi' and pf == 'Pa':
    ptotal = PressureCombos.psitoPa(n)
    print('Pressure in Pa: {0:0.8f}'.format(ptotal))
elif pi == 'Pa' and pf == 'Pa':
    ptotal = n
    print('Pressure in Pa: {0:0.8f}'.format(ptotal))
elif pi == 'psi' and pf == 'psi':
    ptotal = n
    print('Pressure in psi: {0:0.8f}'.format(ptotal))
else:
    print('One or both of your inputs are not a valid pressure type')