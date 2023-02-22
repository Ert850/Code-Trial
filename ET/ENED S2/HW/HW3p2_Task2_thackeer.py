# Activity Python: Homework 3 Part 2 Task 2
# File: HW3p2_Task2_thackeer.py 
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
# Calculates avverage temp over many years and compiles into a list

# Open files
DataFile = open('Task2.txt','r')
ResultsFile = open('Task2_Results.txt','w')

#Read in the data
Data = DataFile.readlines()

#Process the data
ResultsFile.write('{0:5}\t{1:5}\t{2}\n'.format('Year','JanAvg','JulyAvg'))
JAvg = 0
YAvg = 0
d = 0
for k in range(len(Data)):
    Vals = Data[k].split()
    Year = Vals[0]
    Jan = float(Vals[1])
    July = float(Vals[2])
    JAvg = JAvg + Jan
    YAvg = YAvg + July
    d = d + 1
    if d == 31:
        ResultsFile.write('{0:5}\t{1:5.1f}\t{2:.1f}\n'.format(Year,JAvg/31,YAvg/31))
        d = 0
        JAvg = 0
        YAvg = 0

# Close files
DataFile.close()
ResultsFile.close()