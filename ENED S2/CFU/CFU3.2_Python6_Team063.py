# Activity Python: CFU 3.2: Python 6
# File: CFU_Python6_Team063.py 
# Date:    xx January 2023
# By:      Elijah Thacker
# Section: 005
# Team:    063
# 
# ELECTRONIC SIGNATURE
# Elijah Thacker
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# xxx
# Open files
DataFile = open('RC.txt','r')
ResultsFile = open('CFU3.2.txt','w')

#Read in the data
Data = DataFile.readlines()

#Process the data
for k in range(len(Data)):
    if k != 0:
        Vals = Data[k].split()
        Measured = float(Vals[1])
        if Measured > 24:
            ResultsFile.write('{0}\t{1}\t{2}\n'.format(Vals[0],Vals[1],'High'))
        elif Measured < 21:
            ResultsFile.write('{0}\t{1}\t{2}\n'.format(Vals[0],Vals[1],'Low'))
            
# Close files
DataFile.close()
ResultsFile.close()