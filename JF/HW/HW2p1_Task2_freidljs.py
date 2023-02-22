# Assignment
# File:    HW2p1_Task2_freidljs
# Date:    1/26/23
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

sub = input('Enter substance to calculate with (Methanol, Butane, Octane): ')
while sub != 'Methanol' and sub != 'Butane' and sub != 'Octane':
  sub = input('Enter valid substance to calculate with (Methanol, Butane, Octane): ')

meth = [8.0724, 1574.99,238.87,-16,91]
but = [6.0896,935.86,238.73,-78,19]
oct = [6.9094,1349.82,209.385,19,152]

if sub == 'Methanol':
  A = meth[0]
  B = meth[1]
  C = meth[2]
  Tmin = meth[3]
  Tmax = meth[4]

elif sub == 'Butane':
  A = but[0]
  B = but[1]
  C = but[2]
  Tmin = but[3]
  Tmax = but[4]

elif sub == 'Octane':
  A = oct[0]
  B = oct[1]
  C = oct[2]
  Tmin = oct[3]
  Tmax = oct[4]

DeltaT = (Tmax-Tmin)/19

Temp = []

for k in range(20):
  DeltaTCalc = Tmin + k*DeltaT
  Temp.append(DeltaTCalc)

for k in range(len(Temp)):
  Pres = 10**(A-(B/(C+Temp[k])))
  print('Temperature = {0:.3f} (C); Pressure = {1:.3f} (mmHg)'.format(Temp[k],Pres))
