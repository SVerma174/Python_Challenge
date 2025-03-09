""" what is operator in python?
python has many types of operator for different types of operation.
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators

Example:
"""

a=10
b=5
c=a+b
print(c) # it will print the addition of a and b
c=a-b
print(c) # it will print the subtraction of a and b
c=a*b
print(c) # it will print the multiplication of a and b
c=a/b
print(c) # it will print the division of a and b
c=a%b
print(c) # it will print the modulus of a and b (remainder of the division)
c=a**b(if 5**3=125 :  5*5*5=125)
print(c) # it will print the exponentiation of a and b(raise to the power)
c=a//b
print(c) # it will print the floor division of a and b(division of a and b, removing the remainder)

"""
what is Arithmetic operators?
    Arithmetic operators are used with numeric values to perform common mathematical operations:
    +	Addition
    -	Subtraction
    *	Multiplication
    /	Division
    %	Modulus
    **	Exponentiation
    //	Floor division

assignment operators:
    Assignment operators are used to assign values to variables:
    =	x = 5	x = 5
    +=	x += 3	x = x + 3
    -=	x -= 3	x = x - 3
    *=	x *= 3	x = x * 3
    /=	x /= 3	x = x / 3
    %=	x %= 3	x = x % 3
    //=	x //= 3	x = x // 3
    **=	x **= 3	x = x ** 3
    &=	x &= 3	x = x & 3
    |=	x |= 3	x = x | 3
    ^=	x ^= 3	x = x ^ 3
    >>=	x >>= 3	x = x >> 3
    <<=	x <<= 3	x = x << 3

Comparison operators:
    Comparison operators are used to compare two values:
    ==	Equal	x == y
    !=	Not equal	x != y
    >	Greater than	x > y
    <	Less than	x < y
    >=	Greater than or equal to	x >= y
    <=	Less than or equal to	x <= y

Logical operators:
    Logical operators are used to combine conditional statements:
    and 	Returns True if both statements are true	x < 5 and  x < 10
    or	Returns True if one of the statements is true	x < 5 or x < 4
    not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)  

Identity operators:
    Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
    is 	Returns True if both variables are the same object	x is y
    is not	Returns True if both variables are not the same object	x is not y      

Membership operators:
    Membership operators are used to test if a sequence is presented in an object:
    in 	Returns True if a sequence with the specified value is present in the object	x in y
    not in	Returns True if a sequence with the specified value is not present in the object	x not in y 