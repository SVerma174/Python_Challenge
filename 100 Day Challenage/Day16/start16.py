# Match case statemnt 
# 1. Match case statement is used to match a value against a pattern.
# 2. It is similar to switch case statement in other programming languages.
# 3. It is used to match a value against a pattern and execute the code block if the pattern matches.
# 4. It is used to match a value against multiple patterns and execute the code block if any of the patterns match.

# Example:

x = int(input("Enter the x value : "))  # X is a variable and its value is 4

# We use if-elif-else to check the value of x
if x == 1:         # here we check if x is 1
    # If x is 1, this block will be executed
    print("x is 1") # This is the first case
elif x == 2:           # here we check if x is 2
    # If x is 2, this block will be executed
    print("x is 2")   
elif x == 3:           # here we check if x is 3
    # If x is 3, this block will be executed
    print("x is 3")
else:                   # If x is not 1, 2 or 3, this block will be executed
    print("x is not 1, 2 or 3")  # Default case
