""" What is variable in python? 
    # Variables are containers for storing data values.
    # Unlike other programming languages, Python has no command for declaring a variable.
    # A variable is created the moment you first assign a value to it.
    # Variables do not need to be declared with any particular type and can even change type after they have been set.

# Example:
    shubham = "Good Programmer"
    here is shubham is a variable and "Good Programmer" is a value of shubham variable.

variable name rules:
    1. A variable name must start with a letter or the underscore character
    2. A variable name cannot start with a number
    3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    4. Variable names are case-sensitive (age, Age and AGE are three different variables)

variable is nothing but a container that store the data or value.
when we are creating a variable and assign the value to it,
then the variable will store the value value inside the container 
and we can use the variable to access the value,
variable= value
     container store the value in the memory

"""
""" What is data type in python?

    In python data type is nothing but a type of data that we are using in the program.
    there are many data types in python.
    1. Text Type:	str
    2. Numeric Types:	int, float, complex
    3. Sequence Types:	list, tuple, range
    4. Mapping Type:	dict
    5. Set Types:	set, frozenset
    6. Boolean Type:	bool

Example:
"""
# IN Python these are buit-in data types that we can use in the program.

int_data = 10 # int data type
float_data = 10.5 # float data type
complex_data = 1j # complex data type   
str_data = "Hello, World!" # str data type
list_data = ["apple", "banana", "cherry"] # list data type 
tuple_data = ("apple", "banana", "cherry") # tuple data type
range_data = range(6) # range data type
dict_data = {"name" : "shubham", "age" : 25} # dict data type
set_data = {"apple", "banana", "cherry"} # set data type

"""
what is list in python?

    A list is a collection which is ordered and changeable. 
    In Python lists are written with square brackets.
    its bunch of container that store the value or data.
    list is mutable (means we can change the value of list)
Example:
"""
list_data = ["apple", "banana", "cherry"]
print(list_data)

"""
what is tuple in python?

    A tuple is a collection which is ordered and unchangeable. 
    In Python tuples are written with round brackets.
    its bunch of container that store the value or data.
    tuple is immutable (means we can not change the value of tuple)

Example:
""" 
tuple_data = ("apple", "banana", "cherry")
print(tuple_data)

"""
what is set in python?

    A set is a collection which is unordered and unindexed. 
    In Python sets are written with curly brackets.
    its bunch of container that store the value or data.
    set is mutable (means we can change the value of set)
Example:
"""
set_data = {"apple", "banana", "cherry"}
print(set_data)

"""
what is dict in python?

    A dictionary is a collection which is unordered, changeable and indexed. 
    In Python dictionaries are written with curly brackets, and they have keys and values.
    its bunch of container that store the value or data.
    dict is mutable (means we can change the value of dict)
Example:   
"""
dict_data = {"name" : "shubham", "age" : 25}
print(dict_data)



# IN python every thing is object
# object is nothing but a instance of class
# class is nothing but a blueprint of object
# object has properties and methods