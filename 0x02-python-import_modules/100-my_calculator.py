# 100-my_calculator.py

def sum(num1, num2):
    return num1 + num2

def differences(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero"

# Test the calculator functions
num1 = 10
num2 = 5

print("sum:", add(num1, num2))
print("diferences:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
