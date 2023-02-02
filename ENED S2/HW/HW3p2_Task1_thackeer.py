# Activity Python: Homework 3 Part 2 Task 1
# File: HW3p2_Task1_thackeer.py 
# Date:    02 February 2023
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
# Calculates Pressure if Satisfies Condition in a list

# Open files
DataFile = open('Task1.txt','r')
ResultsFile = open('Task1_Results.txt','w')

#Read in the data
Data = DataFile.readlines()

#Process the data
for k in range(len(Data)):
    if k == 0:
        Header = Data[k].split()
        ResultsFile.write('{0:16}\t{1:2}\t{2}\n'.format(Header[0],Header[6],'Pressure'))
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
            ResultsFile.write('{0:15}\t{1:5.0f}\t{2:.2f}\n'.format(Substance,T,P))
        else:
            ResultsFile.write('{0:15}\t{1:5.0f}\t{2}\n'.format(Substance,T,'-9999'))

# Close files
DataFile.close()
ResultsFile.close()