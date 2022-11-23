R = "Y"
while R == "Y":
    print("Loop")
    R = input("Run again? (Y or N): ")
    if R == "n" or R == "N":
        quit()
    elif R == "y" or R == "Y":
        R = "Y"
    else:
        R = 1
        while R == 1:
            R = input("Invalid Entry - Run again? (Y or N): ")
            if R == "n" or R == "N":
                quit()
            elif R == "y" or R == "Y":
                R = "Y"
            else:
                R = 1