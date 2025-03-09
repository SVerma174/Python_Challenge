""" What is type casting in python? 
if we are created a string variable inside there are in double quotes and some values like 27 then if we want to add this number to 3 it will not give result 3o

so we have to convert this string to integer and then add it to 3. this is called type casting.
example:
"""
a = "27"
b = 3
c = a + b  # it will give error typeerror: can only concatenate str (not "int") to str
print(c)

# so we have to convert a to integer
# like this c= int(a) + b
a = "27"
b = 3
c = int(a) + b
print(c)
# so now it will give answer 30

Another example:
if a="4"
b="9"
c=a+b
print(c) # it will give 49 because it will concatenate 4 and 9
# so we have to convert a and b to integer  
a="4"
b="9"   
c=int(a)+int(b)   # here we add in both the variable int so it will convert to integer
print(c) # it will give 13


"""

The convertion of 1 data type to another data types is called as type casting.

There are 3 types of type casting in python
1. Implicit type casting    
2. Explicit type casting

Explicit type casting: 

In this type of type casting we have to convert the data type of the variable manually.
 it means shubham is programmer and he is converting the data type of the variable manually.
example:
"""
a = "27"        
b = 3
c = int(a) + b
print(c) # it will give 30


"""
Implicit type casting:

 In this type of type casting we don't have to convert the data type of the variable manually.
  here is the shubham is not converting the data type of the variable manually
  python automatically convert the data type of the variable.

Example:
"""
a = 27.3
b = 33
c = a + b
print(c) 
"""
# it will give 60.3
here we don't have to convert a to integer python automatically convert it to integer



"""