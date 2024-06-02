# Basic Python
# Python Syntax
# A Python script can be written in Python interactive shell or in the code editor. A Python file has an extension .py.

# Python Indentation
# An indentation is a white space in a text. Indentation in many languages is used to increase code readability, however Python uses indentation to create block of codes. In other programming languages curly brackets are used to create blocks of codes instead of indentation. One of the common bugs when writing python code is wrong indentation.

# Comments
# Comments are very important to make the code more readable and to leave remarks in our code. Python does not run comment parts of our code. Any text starting with hash(#) in Python is a comment.

# Example: Single Line Comment

# Python is eating the world

# Example: Multiline Comment

# Triple quote can be used for multiline comment if it is not assigned to a variable

"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""
# Data types
# In Python there are several types of data types. Let us get started with the most common ones. Different data types will be covered in detail in other sections. For the time being, let us just go through the different data types and get familiar with them. You do not have to have a clear understanding now.

# Number
# Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
# Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
# Complex Example 1 + j, 2 + 4j

# String
# A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

# Example:

'Asabeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challenge'

# Booleans
# A boolean data type is either a True or False value. T and F should be always uppercase.

# Example:

#     True  #  Is the light on? If it is on, then the value is True
#     False # Is the light on? If it is off, then the value is False

# List
# Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.

# Example:

[0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
['Finland','Estonia', 'Sweden','Norway'] # all the same data types - a list of strings (countries)
['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float

# Dictionary
# A Python dictionary object is an unordered collection of data in a key value pair format.

# Example:

# {
# 'first_name':'Asabeneh',
# 'last_name':'Yetayeh',
# 'country':'Finland', 
# 'age':250, 
# 'is_married':True,
# 'skills':['JS', 'React', 'Node', 'Python']
# }

# Tuple
# A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.
# Example:

# ('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names
# ('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets

# Set
# A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.
# In later sections, we will go in detail about each and every Python data type.
# Example:

# {2, 4, 3, 5}
# {3.14, 9.81, 2.7} # order is not important in set

# Python File
# First open your project folder, 30DaysOfPython. If you don't have this folder, create a folder name called 30DaysOfPython. Inside this folder, create a file called helloworld.py. Now, let's do what we did on python interactive shell using visual studio code.

# The Python interactive shell was printing without using print but on visual studio code to see our result we should use a built in function _print(). The print() built-in function takes one or more arguments as follows print('arument1', 'argument2', 'argument3'). See the examples below.

# Example:

# The file name is helloworld.py

# Day 1 - 30DaysOfPython Challenge

# print(2 + 3)             # addition(+)
# print(3 - 1)             # subtraction(-)
# print(2 * 3)             # multiplication(*)
# print(3 / 2)             # division(/)
# print(3 ** 2)            # exponential(**)
# print(3 % 2)             # modulus(%)
# print(3 // 2)            # Floor division operator(//)

#  Checking data types
#  print(type(10))          # Int
#  print(type(3.14))        # Float
#  print(type(1 + 3j))      # Complex number
#  print(type('Asabeneh'))  # String
#  print(type([1, 2, 3]))   # List
#  print(type({'name':'Asabeneh'})) # Dictionary
#  print(type({9.8, 3.14, 2.7}))    # Set
#  print(type((9.8, 3.14, 2.7)))    # Tuple

# Exercise: Level 1
# Check the python version you are using
import platform
print(platform.python_version())
# The version is 3.12.3

# Open the python interactive shell and do the following operations. The operands are 3 and 4.
# addition(+)
3 + 4 
# subtraction(-)
3 - 4 
# multiplication(*)
3 * 4 
# modulus(%)
3 % 4
# division(/)
3 / 4
# exponential(**)
3**4
# floor division operator(//)
3 // 4

# Write strings on the python interactive shell. The strings are the following:
# Your name
my_name = 'Annaliese Tech'
# Your family name
family_name = 'Tech' # My alias last name is Tech
# Your country
my_country = 'United States of America'
# I am enjoying 30 days of python
python_course = 'I am enjoy 30 days of python'

# Check the data types of the following data:
# 10
print(type(10))
# 9.8
print(type(9.8))
# 3.14
print(type(3.14))
# 4 - 4j
print(type(4 - 4j))
# ['Asabeneh', 'Python', 'Finland']
print(type(['Asabeneh', 'Python', 'Finland']))
# Your name
print(type(my_name))
# Your family name
print(type(family_name))
# Your country
print(type(my_country))

# Exercise: Level 2
# Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

# Exercise: Level 3
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# Number
integer_example = 42
float_example = 3.14159
complex_example = 2 + 3j
print(f"Integer: {integer_example}")
print(f"Float: {float_example}")
print(f"Complex: {complex_example}")

# String
string_example = "Hello, World!"
print(f"String: {string_example}")

# Boolean
boolean_example = True
print(f"Boolean: {boolean_example}")

# List
list_example = [1, 2, 3, 4, 5]
print(f"List: {list_example}")

# Tuple
tuple_example = (1, 2, 3, 4, 5)
print(f"Tuple: {tuple_example}")

# Set
set_example = {1, 2, 3, 4, 5}
print(f"Set: {set_example}")

# Dictionary
dictionary_example = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"Dictionary: {dictionary_example}")

# Find an Euclidian distance between (2, 3) and (10, 8)
# Solution 1
import math

# Define points
x1, y1 = 1, 2
x2, y2 = 4, 6

# Calculate Euclidean distance
distance_2d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Euclidean distance in 2D: {distance_2d}")

# Solution 2
# Define points
x1, y1 = 1, 2
x2, y2 = 4, 6

# Step 1: Calculate the differences
diff_x = x2 - x1
diff_y = y2 - y1

# Step 2: Square the differences
square_diff_x = diff_x ** 2
square_diff_y = diff_y ** 2

# Step 3: Sum the squared differences
sum_of_squares = square_diff_x + square_diff_y

# Step 4: Calculate the square root of the sum
distance_2d = sum_of_squares ** 0.5

# Output the result
print(f"Euclidean distance in 2D: {distance_2d}")