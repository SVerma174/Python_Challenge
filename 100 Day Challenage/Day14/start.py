"""
what is if-else statment is python ?

in python if-else statement are decision making startment.
it is also called as conditional control statment.
it execute differente block of code based on certain condition.

example:
"""

a=int(input("Enter your age:"))
print("your age is :",a)

print(a>18)  # it will check age is Greater then 18
print(a<18)     # it will check age is less then 18
print(a==18) # it will check age is equal to equal 18
print(a<=18) # it will check age is less then equal to 18
print(a>=18) # it will chek age is Greater then equal to 18
print(a!=18)# it will chek age is not equal to 18 
 
                #all the values are return in a boolen form

if(a>18):                             # if this condition is true then it will print elgible to drink
    print("you can eligiable for drinking alcohol") 

else:
    print("your not eligible for drink alcohol")  # else it will print not eligble 

"""

here the >,<,== all are conditional operator

# conditional operatotrs
# <,>,>=,<=,==,!=

# if-elif-else
 
-if if condition is true then it will execute if block if not true 
   -it will execute else block 
    -if both the condition or not true then it will execute else block 

example:
"""
a=int(input("Enter your age:"))
print("your age is :",a)


if(a>18):                            # if this condition is true then it will print elgible to drink
    print("you can eligiable for drinking alcohol") 
elif(a>=18):
    print("Your eligible for drink alcohol")
else:
    print("your not eligible for drink alcohol")  # else it will print not eligble 


"""

    ####### Nested if else Staements ######

nested if else statement are inside if-else we can use another if-else statement

# It is used when you need to check multiple conditions that depend on each other.

exaple:

"""
a=int(input("Enter your age:"))
print("your age is :",a)
maturity ="Yes"

if a>=18:
    if maturity == Yes:
        print(" You are eligible to drink bear and alcohol ")
    else:
        print("Your not matured, so you can not drink")
else:
    print("Tum bacche ho abhi, Tum sprite piyyoo ")