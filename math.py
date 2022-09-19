print("This is a program intended to complete simple math functions, like a calculator. It can complete addition, subtraction, multiplication, and division")
number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))
print("Below type 'x' for multplication, '/' for division, '+' for addition, and '-' for subtraction")
function = input("Enter desired function here:")
for i in function:
    if i == "x":
        solution = (number1*number2)
    elif i == "/":
        solution = (number1/number2)
    elif i == "+":
        solution = (number1+number2)
    elif i == "-":
        solution = (number1-number2)
print(solution)
