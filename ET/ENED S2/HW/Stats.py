# Activity Python: Stats
# File: Stats.py 
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
# Statistics Function for test values
def Stats(LStats):
    AVal = 0
    VVal = 0
    for k in range(len(LStats)):
        AVal = LStats[k] + AVal
    Mean = AVal/(len(LStats))
    for k in range(len(LStats)):
        VVal = (LStats[k]-Mean**2+VVal)
    SD = (VVal/(len(LStats)-1))**.5
    return Mean, SD