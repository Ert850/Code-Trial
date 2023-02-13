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

# open files
DataFile = open('Example_Data.txt','r')
ResultsFile = open('Example_Results.txt','w')

# read the data
Data = DataFile.readlines()

# process the data
for k in range(len(Data)):
    if k != 0:
        Vals =Data[k].split()
        Measured = float(Vals[1])
        if Measured > 24:
            ResultsFile.write('{0}\t{1}\t{2}\n'.format(Vals[0],Vals[1],'High'))
        if Measured < 21:
            ResultsFile.write('{0}\t{1}\t{2}\n'.format(Vals[0],Vals[1],'Low'))

# close files
DataFile.close()
ResultsFile.close()