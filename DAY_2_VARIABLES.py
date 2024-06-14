Variables
Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

Python Variable Name Rules

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
Here are some example of valid variable names:

firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2

Invalid variables names

first-name
first@name
first$name
num-1
1num
We will use standard Python variable naming style which has been adopted by many Python developers. Python developers use snake case(snake_case) variable naming convention. We use underscore character after each word for a variable containing more than one word(eg. first_name, last_name, engine_rotation_speed). The example below is an example of standard naming of variables, underscore is required when the variable name is more than one word.

When we assign a certain data type to a variable, it is called variable declaration. For instance in the example below my first name is assigned to a variable first_name. The equal sign is an assignment operator. Assigning means storing data in the variable. The equal sign in Python is not equality as in Mathematics.

Example:

# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

Let us use the print() and len() built-in functions. Print function takes unlimited number of arguments. An argument is a value which we can be passed or put inside the function parenthesis, see the example below.

Example:

print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument

Let us print and also find the length of the variables declared at the top:

Example:

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
Declaring Multiple Variable in a Line
Multiple variables can also be declared in one line:

Example:

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables. Example:

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
Data Types
There are several data types in Python. To identify the data type we use the type built-in function. I would like to ask you to focus on understanding different data types very well. When it comes to programming, it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.

Checking Data types and Casting
Check Data types: To check the data type of certain data/variable we use the type Example:
# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set
Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

Example:

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

Numbers
Number data types in Python:

Integers: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...

Floating Point Numbers(Decimal numbers) Example: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

Complex Numbers Example: 1 + j, 2 + 4j, 1 - 1j

🌕 You are awesome. You have just completed day 2 challenges and you are two steps ahead on your way to greatness. Now do some exercises for your brain and muscles.

# Exercises: Level 1
# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 Days of python programming

# Declare a first name variable and assign a value to it
first_name = 'Annaliese'

# Declare a last name variable and assign a value to it
last_name = 'Bronz'

# Declare a full name variable and assign a value to it
full_name = first_name + ' ' + last_name

# Declare a country variable and assign a value to it
country = 'United States'

# Declare a city variable and assign a value to it
city = 'New York'

# Declare an age variable and assign a value to it
age = 24

# Declare a year variable and assign a value to it
year = 2024

# Declare a variable is_married and assign a value to it
is_married = False

# Declare a variable is_true and assign a value to it
is_true = 'Happy'

# Declare a variable is_light_on and assign a value to it
is_light_on = 'Yes'

# Declare multiple variable on one line
first_name, last_name, country, city, age = 'Annaliese', 'Bronz', 'United States', 'West Babylon', 24
print(first_name, last_name, country, city, age)
print('First name:', first_name)
print('Last name:', last_name)

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(country))
print(type('New York'))
print(type(age))
print(type({'name': 'Annaliese', 'age': 24, 'year': 2024}))
print(type((24, 2024)))
print(type(zip([1,2],[3,4])))
print(type(is_married))
print(type(year))
print(type(is_true))
print(type(is_light_on))
print(type(8j))

# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
print(len(last_name))
len(first_name) - len(last_name)

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
variable_total = num_one + num_two
print("Total:", variable_total)
# Subtract num_two from num_one and assign the value to a variable diff
variable_diff = num_one - num_two
print("Diff:", variable_diff)
# Multiply num_two and num_one and assign the value to a variable product
variable_product = num_two * num_one
print("Product:", variable_product)
# Divide num_one by num_two and assign the value to a variable division
variable_division = num_one / num_two
print("Division:", variable_division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print("Remainder:", remainder)
# Calculate num_one to the power of num_two and assign the value to a variable exp
variable_exp = num_one ** num_two
print("Exp:", variable_exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_divison = num_one // num_two
print("Floor Divison:", floor_divison)

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math

radius = 30
# A = Pi * radius ** 2
area_of_circle = math.pi * 30 ** 2

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# C = 2 * Pi * radius
circum_of_circle = 2 * math.pi  * 30

# Take radius as user input and calculate the area.
user_input = float(input('Enter the radius of a circle: '))
user_area_of_circle = math.pi * user_input ** 2

print("circle:", area_of_circle)
print("circum:", circum_of_circle)
print("Area of circle given by user:", user_area_of_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('First Name: ')
last_name = input('Last Name: ')
country = input('Country: ')
age = input('Age: ')

print("First:", first_name)
print("Last:", last_name)
print("Country:", country)
print("Age:", age)

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')