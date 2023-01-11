# Activity Python: xxx
# File: xxx_thackeer.py 
# Date:    xx November 2022
# By:      Elijah Thacker
# Section: 006
# Team:    088
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
c = 1
v = float(input("Pressure: "))
while c == 1:
    u = input("Units (Pa or psi): ")
    d = input("Convert to (Pa or psi): ")
    if d == "Pa" and u == "psi":
        n = v * 0.000145038
        c = 0
        print("{:0.2f}".format(n), d)
    elif d == "psi" and u == "Pa":
        n = v / 0.000145038
        c = 0
        print("{:0.2f}".format(n), d)
    elif (d == "Pa" and u == "Pa") or (d == "psi" and u == "psi"):
        c = 0
        print("{:0.2f}".format(v), d)
    else:
        c = 1
        print("Incorrect Units")