# Activity Python: HW 2 Part 1 Task 3
# File: HW2p1_Task3_thackeer.py 
# Date:    26 January 2023
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
# Calculate series and parallel and output in a list
list1 = [[100,200],\
    [810,560],\
    [470,360]]
LSeries = []
LParallel = []
for k in range(len(list1)):
    Series = list1[k][0]+list1[k][1]
    Parallel = 1/((1/list1[k][0])+(1/list1[k][1]))
    LSeries.append(Series)
    LParallel.append(Parallel)

for k in range(len(list1)):
    print('R1 = {0}, R2 = {1}, RSeries = {2}, RParallel = {3:0.1f}\n'\
        .format(list1[k][0],list1[k][1], LSeries[k], LParallel[k]))
   