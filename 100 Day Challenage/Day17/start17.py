# For Loop 
# Sometime user need to execute a block of code multiple times

# Eample: 
print(1)
print(2)
print(3)
print(4)

# Like that but it is not efficient to write the same code multiple times
# So we can use for loop to do that

# Based on simplefication there are two types of loops:
# 1. For Loop
# 2. While Loop
# For Loop is used when we know how many times we want to execute a block of code
# And While Loop is used when we don't know how many times we want to execute a block of code
# For Loop is used to iterate over a sequence (list, tuple, dictionary, set, or string), So it means list, tuple ,set and string are iterable objects

# Example:

name= "shubham"      # variable= name , value is = "shubham"
for i in name:   # The for loop is used to go through each character in the string name
    # i is the variable that will take the value of each character in the string name one by one
    # The loop will continue until all characters in the string have been processed
    print(i) # it will print each character of the string name in new line
    if(i=="a"):
        print("This is a is secial character for me")
    # The if statement checks if the current character is "a"
   # then it will print "This is a is secial character for me" after a character
# The output will be:
# s
# h 
# u
# b
# h
# a
#this is a is secial character for me
# m


# Example: list example using for loop

cars=["audi","bmw","mercedes","toyota","honda"]  #here we are created a list of cars variable name cars and value is list of cars
for car in cars:         # The for loop is used to go through each element in the list cars
    print(car) # it will print each element of the list car in new line
    for i in car:   # it will print each character of the string car in new line
        print(i)




# Example: 

for k in range(5):    # Here  we are using range function to create a sequence of numbers from 0 to 4 (5 is not included)
    # The for loop is used to go through each number in the range           
    print(k) # it will print each number of the range in new line
    

# we can also use use argument in range function from where to start and where to end

# Example:
for s in range(3,28):  # Here  we are using range function to create a sequence of numbers from 3 to 27 (28 is not included)
    # The for loop is used to go through each number in the range
    print(s) # it will print each number of the range in new line


# in range function there are three arguments:
# 1. start: The starting number of the sequence (inclusive)
# 2. stop: The ending number of the sequence (exclusive)
# 3. step: The increment between each number in the sequence (optional, default is 1)

# Example:
for t in range(1,10,2):  # Here  we are using range function to create a sequence of numbers from 1 to 9 (10 is not included) with step of 2
    # The for loop is used to go through each number in the range
    print(t) # it will print each number of the range in new line

#so output will be:
# 1
# 3
# 5
# 7
# 9