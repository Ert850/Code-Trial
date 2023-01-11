# Activity Python: Exam 3 Part 25
# File: E3_P25_thackeer.py
# Date:    28 November 2022
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
# Asks user for two constants, q and r, and outputs the combination the sequence will do
# of converging to zero and oscialting, then runs a certain amount of user 
# specified repetitions to determine the last y value in a sequence of calculations

# Allows user to specify constants q and r
q = float(input("Enter Constant 1: "))
r = float(input("Enter Constant 2: "))
# Calculates variable d based on q and r
d = (q ** 2) + (4 * r)
# Runs a series of checks to determine sequence tendencies
# Checks if d is less than 0
if d < 0:
    # If d is less than 0, the sequence oscilates
    print("Sequence Oscilates")
    # If r has a distance from 0 less than 1, then the sequence will converge to 0
    if abs(r) < 1:
        print("Sequence Converges to Zero")
    # If r has a distance from 0 greater than or equal to 1, then the sequence will not converge to 0
    else:
        print("Sequence Converges to Zero")
# Selects all remaining cases, where d is greater than or equal to 1
else:
    # If d is greater than or equal to 0, which it is in this case, the sequence does not oscilate
    print("Sequence Does Not Oscilate")
    # If q is not overcome by the sqrt of d in either scenario below to become greater than 1, then the sequence converges to 0
    if abs((q + (d ** 0.5)) / 2) < 1 and abs((q - (d ** 0.5)) / 2) < 1:
        print("Sequence Converges to Zero")
    # If q is overcome by the sqrt of d in either of the scnearios above to become greater than 1, then the sequence does not converge to 0
    else:
        print("Sequence Does Not Converge to Zero")
# Allows the user to specify the amount of repetitions for calculation to perform
n = int(input("Y-Terms to Compute: "))
# Repeats request until a postitive integer is given
while n <= 0:
    n = int(input("Y-Terms to Compute (give a postitive integer): "))
# Defines yn-1 (starts as y0) as yn1 and yn-2 as yn2
yn1 = 5
yn2 = 0
# Repeats calculations specified count, and utilizes redefining to save values throughout the for loop, bumping values up to become the previous for each loop
for k in range(n):
    y = (q * yn1) + (r * yn2)
    yn2 = yn1
    yn1 = y
# Displays the final y-value
print("Last y-value: ", "{0:.3f}".format(y))