# Activity Python: Homework 14 Part 1 Task 1
# File: HW_14p1_Task1_thackeer.py 
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
# 4 Digit Number Guesser
import random
print("Enter a four digit number, one digit at a time")
D1 = int(input("Digit One: "))
D2 = int(input("Digit Two: "))
D3 = int(input("Digit Three: "))
D4 = int(input("Digit Four: "))
x = 0
cz = 0
co = 0
ct = 0
cr = 0
cf = 0
while x < 1000:
    G1 = random.randint(0,9)
    G2 = random.randint(0,9)
    G3 = random.randint(0,9)
    G4 = random.randint(0,9)
    x = x + 1
    a = 0
    b = 0
    c = 0
    d = 0
    if G1 == D1:
        a = 1
    if G2 == D2:
        b = 1
    if G3 == D3:
        c = 1
    if G4 == D4:
        d = 1
    if a + b + c + d == 0:
        cz = cz + 1
    if a + b + c + d == 1:
        co = co + 1
    if a + b + c + d == 2:
        ct = ct + 1
    if a + b + c + d == 3:
        cr = cr + 1
    if a + b + c + d == 4:
        cf = cf + 1
print("0 Correct: ",cz,", 1 Correct: ",co,", 2 Correct:",ct,", 3 Correct: ",cr,", 4 Correct: ",cf)