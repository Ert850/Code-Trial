import math
print("This is a program intended to complete simple math functions, like a calculator")
print("It can complete addition, subtraction, multiplication, and division")
print("In later sections it can do natural logs, numbers to a power, and basic trigonometry")
print("This is the division, multiplication, addition, and subtration section:")
number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))
function = input("Enter 'x' for multplication, '/' for division, '+' for addition, and '-' for subtraction: ")
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
print("This is the natural log section:")
ln = log(float(input("To solve a natural log, input the number here (Enter a number above 0): ")))
print(ln)
print("Below you'll be able to solve for numbers to a power in the form x^y")
x = float(input("Enter the base: "))
y = float(input("Enter the power: "))
print(x**y)
print("This is the triogonmetry section:")
selection = input("Type 's' for sin, 'c' for cos, 't' for tan, and 'x-' for any of the previous functions inverse: ")
v = float(input("Enter a value to compute. Keep in mind the range of trigonometric functions when inputing your value: "))
for i in selection:
    if i == "s":
        answer = (sin(v))
    elif i == "c":
        answern = (cos(v))
    elif i == "t":
        answer = (tan(v))
    elif i == "s-":
        answer = (1/sin(v))
    elif i == "c-":
        answer = (1/cos(v))
    elif i == "t-":
        answer = (1/tan(v))
print(answer)
