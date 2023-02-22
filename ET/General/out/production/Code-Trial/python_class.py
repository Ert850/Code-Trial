# Create a variable for cost of meal, tax and tip and assign their values
# Note that percentage is not captured in programming languages. Divide by 100 instead. 
cost_of_meal = 54.76
tax = 0.0785
tip = 0.15

# Calculate tax amount by creating a variable for it and assign it to a formula using the variables for cost of meal and tax
tax_amount = tax * cost_of_meal

# Calculate cost after tax
cost_after_tax = cost_of_meal + tax_amount

# Calculate tip amount
# Hint: Calculate the tip amount the cost after tax
tip_amount = 0.15 * cost_after_tax

# Calculate total amount
total = cost_after_tax + tip_amount

print('My original meal cost is', cost_of_meal)

# Follow the example above and print the tax amount
print('Tax amount is: ', tax_amount)

# Print the cost after tax
print('Cost after tax is: ', cost_after_tax)

# Print the tip amount
print('Tip amount is: ', tip_amount)

# Print the total cost of the meal
print('Total cost is: ', total)

first = input("Enter first number: ")
second = input("Enter second number: ")
print(first == second)

third = input("first number: ")
fourth = input("second number: ")
fifth = input("third number: " )
all_equal = (third == fourth == fifth)
print("All are equal is :", all_equal)
any_equal = (third == fourth or fourth == fifth or third == fifth)
print("Any of the three are equal:", any_equal)