# Activity Python: Homework 3 Part 
# File: xxx_thackeer.py 
# Date:    xx January 2023
# By:      Elijah Thacker
# Section: 006
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
DataFile = open('Task1.txt','r')
ResultsFile = open('Pressure.txt','w')

#Read in the data
Data = DataFile.readlines()

#Process the data
for k in range(len(Data)):
    if k == 0:
        Header = Data[k].split()
        ResultsFile.write('{0}\t{1}\t{2}\n'.format(Header[0],Header[6],'Pressure'))
    elif k != 0:
        Vals = Data[k].split()
        Substance = Vals[0]
        A = float(Vals[1])
        B = float(Vals[2])
        C = float(Vals[3])
        Tmin = float(Vals[4])
        Tmax = float(Vals[5])
        T = float(Vals[6])
        P = 10**(A-(B/(C+T)))
        if Tmax > T and T > Tmin:
            ResultsFile.write('{0}\t{1}\t{2}\n'.format(Substance,T,P))
        
# Close files
DataFile.close()
ResultsFile.close()