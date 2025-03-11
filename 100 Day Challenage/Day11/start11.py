""" What is string in python? 
Anything which you written in double quotes or single quotes is called string.
"""
name="shubham"
print(name) # shubham

name='shubham'
print(name) # shubham


# here single quotes and double quotes are same it doesn't matter which one you use.
"""
You can not use doube quotes inside double quotes and single quotes inside single quotes.

car="I'm going to market""shubham"
print(car) # SyntaxError: invalid syntax


instant of that if we use or run that code 
we use backslash(\) to escape the quotes.
"""
car="I'm going to market ,\"shubham"
print(car) # I'm going to marketshubham


"""
2nd method 
is use single quotes inside double quotes and double quotes inside single quotes.

"""
car="I'm going to market'shubham"
print(car) # I'm going to market'shubham
"""



What is string indexing?
Indexing means to access the element of the string.
it start from 0 to n-1 where n is the length of the string.


example:
"""
name="shubham"

print(shubham[0]) # s  it will print the first element of the string which in the 0 position 
print(shubham[1]) # h
"""

Negative indexing:
Negative indexing means to access the element of the string from the last.
it start from -1 to -n where n is the length of the string.

example:"""
name="shubham"
print(shubham[-1]) # m  it will print the last element of the string which in the -1 position
print(shubham[-2]) # a


"""
what is for loop?
for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.


example: 
"""
for i in "shubham":
    print(i)

# output:
# s
# h 
# u
# b
# h
# a
# m

# it will print the each element of the string or each index of the string.
"""
