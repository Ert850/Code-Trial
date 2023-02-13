# Assignment
# File:    HW3p2_Task1_freidljs
# Date:    2/1/23
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

Data = open('Task1.txt','r')
Results = open('Task1_Results.txt','w')

data = Data.readlines()

Results.write('{0:5}\t{1:5}\t{2}\n'.format('Substance','T','P'))
for k in range(len(data)):
    Vals = data[k].split()
    Substance = Vals[0]
    A = float(Vals[1])
    B = float(Vals[2])
    C = float(Vals[3])
    Tmin = float(Vals[4])
    Tmax = float(Vals[5])
    T = float(Vals[6])
    P = 10**(A-(B/(C+T)))
    if Tmax > T and T > Tmin:
        Results.write('{0:15}\t{1:5.0f}\t{2:.0f}\n'.format(Substance,T,P))
    else:
        Results.write('{0:15}\t{1:5.0f}\t{2:.0f}\n'.format(Substance,T,-9999))

Data.close()
Results.close()