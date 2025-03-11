""" String operations ?
# what is string method 

string methods are used to perfrom operations onstring we can manipulate, formet, and analyze the string data using stings method.

# string method or called using (.) notation ...string.method()

python a set of bulit-in method using we can perform operation like alter and modify.

#VERY VERY IMPORTANT AS A POV OF INTERVIEW

# strings are immutable , but we can change the string but it will not change the exact
        string it create copy or newly string.


1).upper() : it will convert the string into Upper case 

Example:
"""
a="shubham"
print(a)
print(a.upper()) # here it will not converted the a="shubham" to SHUBHAM
                # it was created new string with changes 
"""
2).lower(): it convert all charcter in lowercase

example:
"""
a="SHUBHAM"
print(a.lower())

"""
3).replace() : it will replace the string 

example:

"""
a="shubham"
print(a.replace('bh','kt'))

""" 
4).find(): it will find the position of substring

Example:
"""
s="shubham"
print(s.find('a')) # it will find the a index number of that character

"""
5).split(): it will split a string into list

example:
"""
shubh="Great,python,programmer"
print(shubh.split(','))

"""
6).center(): it will align the string in to center as per the parameter given by the user

example:
"""
s="shubham is a Great python programmer"
print(s.center(40))

"""
7).count(): count method is count the nuber of valur occured in how many times

example:"""
s="shubham is a Great python programmer"
print(s.count('m'))
