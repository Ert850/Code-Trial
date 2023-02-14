# Activity Python: Exam 4 Part 20
# File: E4_P20_thackeer.py 
# Date:    13 February 2023
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
# Read Robot txt file and output data
# Open files
DataFile = open('Robot.txt','r')
ResultsFile = open('E4_thackeer.txt','w')

#Read in the data
Data = DataFile.readlines()

#Process the data
xc = 0
yc = 0
bc = 0
ResultsFile.write('{0}\t{1}\n'.format("Xerror","Yerror"))
for k in range(len(Data)):
    Vals = Data[k].split()
    x = float(Vals[0])
    y = float(Vals[1])
    xerror = x - 19.3125
    yerror = y - 59
    ResultsFile.write('{0:5.4f}\t{1:.4f}\n'.format(xerror,yerror))
    if ((x < 19.5 or x == 19.5) or (x > 19.125 or x == 19.125)) and ((y < 59 or x == 59) or (y > 58 or y == 58)):
        bc = bc + 1
    elif ((x < 19.5 or x == 19.5) or (x > 19.125 or x == 19.125)):
        xc = xc + 1
    elif ((y < 59 or x == 59) or (y > 58 or y == 58)):
        yc = yc + 1
print("Count X: ",xc,"Count Y: ",yc, "Count Both: ",bc)
       
# Close files
DataFile.close()
ResultsFile.close()