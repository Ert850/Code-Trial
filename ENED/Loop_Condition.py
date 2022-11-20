R = "Y"
while R == "Y":
    print("Loop")
    R = input("Run again? (Y or N): ")
    if R == "y":
        R = "Y"
    elif R == "Y":
        R = "Y"
    elif R == "n":
        quit()
    elif R == "N":
        quit()
    else:
        R = 1
        while R == 1:
            R = input("Invalid Entry - Run again? (Y or N): ")
            if R == "y":
                R = "Y"
            elif R == "Y":
                R = "Y"
            elif R == "n":
                quit()
            elif R == "N":
                quit()
            else:
                R = 1