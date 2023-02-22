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

RC = open('RC.txt','r')
CFU = open('CFU3p2.txt','w')

rc = RC.readlines()
maxtau = 0
tau = []
for k in range(len(rc)):
    Vals = rc[k].split()
    r = (Vals[0])
    c = (Vals[1])
    t = r*c
    tau.append[t]
    if tau[k] > maxtau:
      maxtau = tau[k]

print('{0:.2f}'.format(maxtau))
CFU.write(str(round('{0:.2f}'.format(tau))))

RC.close()
CFU.close()
