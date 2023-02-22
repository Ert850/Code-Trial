# Take input for DNA string and store in a variable DNA_string
DNA_string = input("Give the input DNA Code : ")

# Intialize the RNA output as an empty string
RNA_string = ''

# Use "for" loop to traverse the DNA string. Use "If..elif..else" sub block to check and concactenate the appropriate letter 
# to RNA_string.
# Use "else" block in the "If..elif..else" sub block to output an error message and break if a diffrent letter is encountered

for i in DNA_string.upper():
    # the upper() method is used to make our program case insensitive
    if i == 'G':
        RNA_string = RNA_string + 'C'
    # Continue the "elif" blocks of the "If..elif..else" block for the other letters
    elif i == 'C':
        RNA_string = RNA_string + 'G'
    elif i == 'A':
        RNA_string = RNA_string + 'T'
    elif i == 'T':
        RNA_string = RNA_string + 'A'
    # Complete the "If..elif..else" block with "else" block for an error message assigned to RNA_string 
    # break out of the loop    
    else: 
        RNA_string = 'Incorrect DNA string'
        break
else:
    # This else is attached to the for loop
    print('Done with Translation')

print('DNA output: ', RNA_string)