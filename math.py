from cmath import log, log10
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
ln = log(float(input("To solve a natural log, input the number here (Enter a number above 0): ")))
print(ln)
print("Below you'll be able to solve for numbers to a power in the form x^y")
x = float(input("Enter the base: "))
y = float(input("Enter the power: "))
print(x^y)