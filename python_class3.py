def uc_6_2(first_name,last_name):
    # Use the appropriate If and else Decision Block with a condition that compares the Length of the Last name
    # In the If and else Decision Block store the six plus two in a variable
    # Use the Tips below in your If and else Decision Block
    if len(last_name) >= 6:
        sixplus2 = last_name[0:6] + first_name[0] + first_name[-1]        
    # Continue the "If..elif..else" block with the appropriate block for the remaining scenario
    else:
        sixplus2= last_name + first_name[0:(6-len(last_name)+1)] + first_name[-1]
    # Return the six plus two in lower case
    return(sixplus2.lower())


# Tips (Replace the portions marked as with ?)
# ********************************************
# For length of the last name is >=6, sixplus2 = last_name[0:?] + first_name[0] + first_name[?]
# For length of the last name is <6, sixplus2 = last_name + first_name[0:(6-len(?)+1)] + first_name[?]