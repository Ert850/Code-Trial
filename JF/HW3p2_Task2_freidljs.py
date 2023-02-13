# Assignment
# File:    HW3p2_Task2_freidljs
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

Data = open('Task2.txt','r')
Results = open('Task2_Results.txt','w')

data = Data.readlines()
counter = 0
JanAvg = 0
JulyAvg = 0

Results.write('{0:5}\t{1:5}\t{2}\n'.format('Year','JanAvg','JulyAvg'))
for k in range(len(data)):
    Vals = data[k].split()
    Jan = float(Vals[1])
    July = float(Vals[2])
    JanAvg = JanAvg+Jan
    JulyAvg = JulyAvg+July
    counter = counter+1
    if counter == 31:
        Results.write('{0:5}\t{1:5.1f}\t{2:.1f}\n'.format(Vals[0],JanAvg/31,JulyAvg/31))
        counter = 0
        JanAvg = 0
        JulyAvg = 0

Data.close()
Results.close()