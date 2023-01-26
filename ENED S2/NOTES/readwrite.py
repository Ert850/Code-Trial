# Activity Python: xxx
# File: xxx_thackeer.py 
# Date:    xx January 2022
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
# example

# Open files
DataFile = open('Example_Data.txt','r')
ResultsFile = open('Example_Results.txt','w')

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