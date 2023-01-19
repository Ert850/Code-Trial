# Activity Python: Alloys
# File: Alloys.py 
# Date:    18 January 2023
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
# Computes and returns the total cost for the # of pounds and cost of a specified alloy
def CostCalc(AlloyNum,Count):
    if AlloyNum == 356:
        Cost = Count * 1.36697
    elif AlloyNum == 2048:
        Cost = Count * 1.28049
    elif AlloyNum == 7075:
        Cost = Count * 1.24355
    return Cost