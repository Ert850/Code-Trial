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
import SpringCombos

k1 = float(input('Enter first spring constant (N/m): '))
k2 = float(input('Enter second spring constant (N/m): '))
ftotal = float(input('Enter the total force (N): '))
conf = input('Enter configuration type (series or parallel): ')

if k1 < 0 or k2 < 0 or ftotal < 0:
    print('Error: Invalid inputs')

if conf == 'series':
    keq = SpringCombos.Keqseries(k1,k2)
    f1 = SpringCombos.F1series(ftotal)
    f2 = SpringCombos.F2series(ftotal)
    x1 = SpringCombos.X1series(k1,f1)
    x2 = SpringCombos.X2series(k2,f2)
    xtotal = SpringCombos.Xtotalseries(keq,ftotal)

if conf == 'parallel':
    keq = SpringCombos.Keqparallel(k1,k2)
    x1 = SpringCombos.X1parallel(k1,f1)
    x2 = SpringCombos.X2parallel(k2,f2)
    xtotal = SpringCombos.Xtotalparallel(keq,ftotal)
    f1 = SpringCombos.F1parallel(ftotal)
    f2 = SpringCombos.F2parallel(ftotal)

print('The value for Keq is: {0:0.2f}'.format(keq))
print('The value for F1 is: {0:0.2f}'.format(f1))
print('The value for F2 is: {0:0.2f}'.format(f2))
print('The value for X1 is: {0:0.2f}'.format(x1))
print('The value for X2 is: {0:0.2f}'.format(x2))
print('The value for Xtotal is: {0:0.2f}'.format(xtotal))