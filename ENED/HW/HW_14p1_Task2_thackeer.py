# Activity Python: Homework 14 Part 1 Task 2
# File: HW_14p1_Task2_thackeer.py 
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
# Simulate a two player dice game
import random
p1 = 0
p2 = 0
turn = 1
while (p1 < 50) or (p2 < 50):
    while turn == 1:
        if (p1 < 50):
            r1 = random.randint(1,6)
            r2 = random.randint(1,6)
            print("Dice 1: ", r1, "Dice 2: ", r2)
            if r1 == 5 or r2 == 5:
                turn = 0
                print("Player 1 - your turn is over")
            else:
                p1 = p1 + r1 + r2
                print("Player 1 Score", p1)
        else:
            print("The Winner is Player 1")
            print("Player 1 Final Score: ", p1)
            print("Player 2 Final Score: ", p2)
            quit()
    while turn == 0:
        if (p2 < 50):    
            r1 = random.randint(1,6)
            r2 = random.randint(1,6)
            print("Dice 1: ", r1, "Dice 2: ", r2)
            if r1 == 5 or r2 == 5:
                turn = 1
                print("Player 2: your turn is over")
            else:
                p2 = p2 + r1 + r2
                print("Player 2 Score", p2)
        else:
            print("The Winner is Player 2")
            print("Player 1 Final Score: ", p1)
            print("Player 2 Final Score: ", p2)
            quit()