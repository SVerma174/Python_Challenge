# Creating calculator which is capable of performing addition, subtraction, multiplication, and division.
# Operation on two numbers, Your program should output in a readable manner.

# Basic calculator

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Enter the operation you want to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Enter the operation: ")

if operation == "1":
    print("Addition of two numbers is: ", a + b)
elif operation == "2":
    print("Subtraction of two numbers is: ", a - b)
elif operation == "3":
    print("Multiplication of two numbers is: ", a * b)
elif operation == "4":
    print("Division of two numbers is: ", a / b)
elif operation.lower() == "exit":
    print("Thank you for using the calculator")
else:
    print("Enter a valid operation")