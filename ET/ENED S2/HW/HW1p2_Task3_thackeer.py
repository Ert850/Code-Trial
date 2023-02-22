# Activity Python: HW1p2_Task3_thackeer
# File: HW1p2_Task3_thackeer.py 
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
# Alloy Cost Ouputer
import Alloys

AlloyNum = float(input("Enter Alloy Type (356, 2048, or 7075): "))
while AlloyNum != 356 and AlloyNum != 2048 and AlloyNum != 7075:
    if AlloyNum != 356 and AlloyNum != 2048 and AlloyNum != 7075:
        AlloyNum = float(input("Enter Alloy Type (356, 2048, or 7075): "))
Count = float(input("Pounds: "))
while Count <= 0:
    if Count <= 0:
        Count = float(input("Pounds (Positive Number): "))
        
Cost = Alloys.CostCalc(AlloyNum,Count)
print("{:0.2f}".format(Cost))