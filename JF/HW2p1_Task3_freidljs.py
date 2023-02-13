# Assignment
# File:    HW2p1_Task3_freidljs
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

R = [[100,200],\
    [810,560],\
    [470,360]]
Rseries = []
Rparallel = []

for k in range(len(R)):
    Rs = R[k][0]+R[k][1]
    Rp = 1/((1/R[k][0])+(1/R[k][1]))
    Rseries.append(Rs)
    Rparallel.append(Rp)

for k in range(len(R)):
    print('R1 = {0}; R2 = {1}; Rseries = {2}; Rparallel = {3:.1f}'.format(R[k][0],R[k][1],Rseries[k],Rparallel[k]))