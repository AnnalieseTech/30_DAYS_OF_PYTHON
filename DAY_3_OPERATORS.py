# Boolean
# A boolean data type represents one of the two values: True or False. The use of these data types will be clear once we start using the comparison operator. The first letter T for True and F for False should be capital unlike JavaScript. Example: Boolean Values

print(True)
print(False)

# Operators
# Python language supports several types of operators. In this section, we will focus on few of them.

# Assignment Operators
# Assignment operators are used to assign values to variables. Let us take = as an example. Equal sign in mathematics shows that two values are equal, however in Python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable. The table below shows the different types of python assignment operators, taken from w3school.

# Assignment Operators

# Arithmetic Operators:

# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b
# Modulus(%): a % b
# Floor division(//): a // b
# Exponentiation(**): a ** b

# Arithmetic Operators

# Example:Integers

# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2

# Example:Floats

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
Example:Complex numbers

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# Let's declare a variable and assign a number data type. I am going to use single character variable but remember do not develop a habit of declaring such types of variables. Variable names should be all the time mnemonic.

# Example:

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponentiation)
Example:

print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

# Let us start start connecting the dots and start making use of what we already know to calculate (area, volume,density, weight, perimeter, distance, force).

# Example:

# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3

# Comparison Operators
# In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value. The following table shows Python comparison operators which was taken from w3shool.

# Comparison Operators Example: Comparison Operators

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# In addition to the above comparison operator Python uses:

# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# Logical Operators
# Unlike other programming languages python uses keywords and, or and not for logical operators. Logical operators are used to combine conditional statements:

# Logical Operators

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

# 🌕 You have boundless energy. You have just completed day 3 challenges and you are three steps ahead on your way to greatness. Now do some exercises for your brain and your muscles.

# Declare your age as integer variable
age_of_Annaliese = 24
# Declare your height as a float variable
height_of_Annaliese = 5.25
# Declare a variable that store a complex number
complex_num = 100j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
enter_base = float(input("Enter a base number: "))
enter_height = float(input("Enter a height number: "))

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# area of a triangle
# area = 0.5 x b x h
area_of_a_triangle = 0.5 * enter_base * enter_height
print('The area of the triangle is:', area_of_a_triangle)

side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
# Perimeter of a triangle
# perimeter = a + b + c
triangle_perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is:', triangle_perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("length: "))
width = int(input("width: "))
# width of a rectangle
# area = length x width
area = length * width
# Perimeter of a rectangle
# perimeter = 2 x (length + width)
perimeter = 2 * (length + width)
print('Area of the triangle is:', area)
print('Perimeter of the triangle is:', perimeter)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# area of a circle
# area = pi x r x r
radius = float(input("Enter radius: "))
area_of_a_circle = math.pi * radius * radius
print('the area of a circle with the input of {} results in {}'.format(radius, area_of_a_circle))
# circumference of a circle
# c = 2 x pi x r
circumference = float(input("Enter: "))
circumference_of_a_circle = 2 * math.pi * radius 
print('the circumference of a circle with the input of {} results in {}'.format(radius, circumference_of_a_circle))

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# y = mx + b
equation_1 = 'y = 2x-2'
slope = 2
y_intercept = -2

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x_intercept = y_intercept / slope
print('The x-intercept is {} with a slope of {} and a y-intercept of {}'.format(x_intercept, slope, y_intercept))

# Find the slope
x1 = 2
y1 = 2
x2 = 6
y2 = 10

slope_m = (y2 - y1) / (x2 - x1)
print('x1 as {}, y1 as {}, x2 as {}, and y2 as {} result in the slope of {}'.format(x1, y1, x2, y2, slope_m))

# Euclidean distance
# D = (x2 - x1)^2 + (y2 - y1)^2
x1 = 2
x2 = 2
y1 = 6
y2 = 10

euclidean_distance = (x1 - x2) * 2 + (y1 - y2) * 2
slope = (y2 - y1)**1/2 / (x2 - x1)**1/2
print('x1 as {}, y1 as {}, x2 as {}, y2 as {} result with slope {}'.format(x1, y1, x2, y2, slope))
print('The Euclidean Distance is calculated at {}'.format(euclidean_distance))

# Compare the slopes in tasks 8 and 9.
slope_m = 7.66
slope_2 = 2
print(slope_m > slope_2)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# y = x**2 + 6x + 9
# Define the quadratic equation
def quadratic_equation(x):
    return x**2 + 6*x + 9

# Test different x values
x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Calculate corresponding y values
y_values = [quadratic_equation(x) for x in x_values]

# Print the results
for x, y in zip(x_values, y_values):
    print(f"For x = {x}, y = {y}")

# Find the x value when y is 0
zero_x_value = -3

# Verify y is 0 at the found x value
zero_y_value = quadratic_equation(zero_x_value)

print(f"\nFor x = {zero_x_value}, y = {zero_y_value}")

# Define the quadratic equation function
def quadratic_equation(x):
    return x**2 + 6*x + 9

# Test different x values
x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Calculate and print corresponding y values
for x in x_values:
    y = quadratic_equation(x)
    print(f"For x = {x}, y = {y}")

# Find the x value when y is 0
zero_x_value = -3

# Verify y is 0 at the found x value
zero_y_value = quadratic_equation(zero_x_value)

print(f"\nFor x = {zero_x_value}, y = {zero_y_value}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') == len('dragon'))
print(len('python') < len('dragon'))
print(len('python') > len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

print('To check if in is in jargon', 'on' in 'jargon')
print('on' != 'python' and 'dragon')

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
dragon_string = "dragon"
python_string = "python"

# There is no 'on' in both dragon and python
is_on_in_dragon = 'on' in dragon_string
is_on_in_python = 'on' in python_string

# Print the results
print(f"Is 'on' in dragon: {is_on_in_dragon}")
print(f"Is 'on' in python: {is_on_in_python}")

# Find the length of the text python and convert the value to float and convert it to string
print(len('python'))
len_python = 6
len_to_float = float(len_python)
print('len_to_float:', len_to_float)
len_to_string = str(len_python)
print('len_to_string:', len_to_string)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Test the function
number_to_check = 10
result = is_even(number_to_check)

# Print the result
print(f"Is {number_to_check} even? {result}")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division_result = 7 // 3

# Integer conversion of 2.7
int_of_2_7 = int(2.7)

# Check if the two values are equal
is_equal = floor_division_result == int_of_2_7

# Print the result
print(f"Is the floor division of 7 by 3 equal to the int converted value of 2.7? {is_equal}")

# Check if type of '10' is equal to type of 10
print(type(10))
ten = 10
is_equal_or_not = ten == int
print(is_equal_or_not)

# Check if int('9.8') is equal to 10
is_equal_types = type('9.8') == type(10)
print(f"Is the type of '9.8' equal to the type of 10? {is_equal_types}")

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120

hours = int(input("Enter hours: "))
rate_per_hour = float(input("Rate per hour: "))
weekly_earning = hours * rate_per_hour
print(f"Your weekly earning is {weekly_earning}")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
num_of_years = int(input("Enter number of years: "))
in_a_year = 365 * 24 * 60 * 60
calculate = num_of_years * in_a_year
print(calculate)

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print('1 1 1 1 1')
print('5 1 5 25 125')
print('5 1 5 25 125')
print('5 1 5 25 125')
print('5 1 5 25 125')

print('1 1 1 1 1',
      '2 1 2 4 8',
      '3 1 3 9 27',
      '4 1 4 16 64',
      '5 1 5 25 125', sep='\n')

# Display the header
print("Number  1^1  1^2  1^3  1^4")

# Display the table
for number in range(1, 6):
    print(f"{number} {1} {number} {number**2} {number**3}")


# Define the number of rows
num_rows = 5

# Loop to display each row
for i in range(1, num_rows + 1):
    # Initialize the row string with the first value
    row_string = str(i)

    # Add the calculated values to the row string
    for j in range(4):
        row_string += ' ' + str(i**j)

    # Print the row
    print(row_string)