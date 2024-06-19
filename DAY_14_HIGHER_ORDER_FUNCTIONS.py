# Higher Order Functions
# In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable

# In this section, we will cover:
# Handling functions as parameters
# Returning functions as return value from another functions
# Using Python closures and decorators

# Function as a Parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

# Function as a Return Value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

# You can see from the above example that the higher order function is returning different functions depending on the passed parameter

# Python Closures
# Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. Let us have a look at how closures work in Python. In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. See the example below.

# Example:

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

# Python Decorators
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

# Creating Decorators
# To create a decorator function, we need an outer function with an inner wrapper function.

# Example:

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

# Applying Multiple Decorators to a Single Function
'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

# Accepting Parameters in Decorator Functions
# Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters.

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

# Built-in Higher Order Functions
# Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce. Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.

# Python - Map Function
# The map() function is a built-in function that takes a function and iterable as parameters.

    # syntax
    # map(function, iterable)

# Example:1

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
Example:2

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
Example:3

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# What actually map does is iterating over a list. For instance, it changes the names to upper case and returns a new list.

# Python - Filter Function
# The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.

    # syntax
    # filter(function, iterable)

Example:1

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

# Example:2

numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']

# Python - Reduce Function
# The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value. Example:1

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

# Exercises: Day 14
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1
# Explain the difference between map, filter, and reduce.
"""Answer:

The map() function is a built-in function that takes a function and iterable as parameters.

The filter() function calls the specified function which returns boolean for each item of 
the specified iterable (list). It filters the items that satisfy the filtering criteria.

The reduce() function is defined in the functools module and we should import it from this
module. Like map and filter functions. it takes two parameters - a function and an iterable.
However, it does not return another iterable. It instead returns a single value. Example: 1.    
"""
# Explain the difference between higher order function, closure and decorator
"""Answer:

A higher order function is where python functions are treated as first class citizens, allowing you to perform the following functions:
-A function can take one or more functions as parameters
-A function can be returned as a result of another function
-A function can be modified
-A function can be assigned to a variable
A closure is when python allows a nested function to access the outer scope of the enclosing function.
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 
"""
# Define a call function before map, filter or reduce, see examples.
# Map
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# Filter
def is_even(x):
    return x % 2 == 0

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

# Reduce
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

# Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def country_list(country_loop):
    for count in country_loop:
        print(count)

country_list(countries)

# Use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def names_list(name_loop):
    for name in name_loop:
        print(name)

names_list(names)

# Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def numbers_list(numbers_loop):
    for number in numbers_loop:
        print(number)

numbers_list(numbers)

Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def change_to_upper(country):
    return country.upper()

names_upper_cased = map(change_to_upper, countries)
print(list(names_upper_cased))

# Lambda function version
names_upper_cased = map(lambda country: country.upper(), countries)
print(list(names_upper_cased))

# Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def change_to_square(number):
    return number ** 2

num_to_square = map(change_to_square, numbers)
print(list(num_to_square))

# Lambda function version
num_to_square = map(lambda number: number ** 2, numbers)
print(list(num_to_square))

# Use map to change each name to uppercase in the names list
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))

# Use filter to filter out countries containing 'land'.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def land(string):
    return 'land' in string

countries_with_land = list(filter(land, countries))
print(countries_with_land)

# Use filter to filter out countries having exactly six characters.
def six_characters(string):
    return len(string) == 6

countries_with_six_characters = list(filter(six_characters, countries))
print(countries_with_six_characters)

# Use filter to filter out countries containing six letters and more in the country list.
def six_or_more(string):
    return len(string) > 6

six_or_more = list(filter(six_or_more, countries))
print(six_or_more)

# Use filter to filter out countries starting with an 'E'
def no_e(string):
    return string[0] == "E"

start_with_e = list(filter(no_e, countries))
print(start_with_e)

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# Initial list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Use map to square each number
squared_numbers = [x * x for x in numbers]

# Step 2: Use filter to keep only even numbers
even_squares = [x for x in squared_numbers if x % 2 == 0]

# Step 3: Implement a custom reduce function to sum the remaining numbers
def custom_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = func(value, element)
    return value

# Use the custom reduce function to sum the even squares
sum_of_even_squares = custom_reduce(lambda x, y: x + y, even_squares)

# Output the result
print(sum_of_even_squares)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(input_list):
    # Use list comprehension to filter out only string items
    string_items = [item for item in input_list if isinstance(item, str)]
    return string_items

# Example usage:
mixed_list = [1, 'apple', 3.14, 'banana', True, 'cherry']
result = get_string_lists(mixed_list)
print(result)  # Output: ['apple', 'banana', 'cherry']

# Use reduce to sum all the numbers in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define a custom reduce function to sum all the numbers in the list
def reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = func(value, element)
    return value

# Use the custom reduce function with a lambda to sum the numbers
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Print the result
print(sum_of_numbers)
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# List of countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# Initialize an empty string to store the concatenated countries
concatenated_countries = ""

# Iterate through the countries and concatenate them with commas
for index, country in enumerate(countries):
    concatenated_countries += country
    if index < len(countries) - 2:
        concatenated_countries += ', '  # Add comma and space for all countries except the last two
    elif index == len(countries) - 2:
        concatenated_countries += ', and '  # Add 'and' before the last country

# Produce the desired sentence
sentence = f'{concatenated_countries} are north European countries.'

# Print the result
print(sentence)
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries():
    # List of countries
    countries = ['Finland', 'Iceland', 'Thailand', 'Nigeria', 'Poland', 'Pakistan', 'India', 'Ireland', 'Afghanistan', 'Australia']

    # Initialize empty lists for each category
    land_countries = []
    ia_countries = []
    island_countries = []
    stan_countries = []

    # Categorize countries based on patterns
    for country in countries:
        if 'land' in country.lower():
            land_countries.append(country)
        elif country.endswith('ia'):
            ia_countries.append(country)
        elif 'island' in country.lower():
            island_countries.append(country)
        elif country.endswith('stan'):
            stan_countries.append(country)

    # Return the categorized lists
    return {
        'land_countries': land_countries,
        'ia_countries': ia_countries,
        'island_countries': island_countries,
        'stan_countries': stan_countries
    }

# Call the function and store the result
categorized_countries = categorize_countries()

# Print the categorized lists
print(categorized_countries)
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_countries_by_letter(countries_list):
    # Initialize an empty dictionary to store the count of countries for each starting letter
    letter_counts = {}

    # Count the countries for each starting letter
    for country in countries_list:
        first_letter = country[0].upper()  # Get the first letter and convert to uppercase
        if first_letter in letter_counts:
            letter_counts[first_letter] += 1
        else:
            letter_counts[first_letter] = 1

    return letter_counts

# Example list of countries
countries = ['Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Italy', 'Japan', 'Russia', 'Spain', 'Sweden']
# Call the function with the countries list and store the result
country_counts = count_countries_by_letter(countries)
# Print the dictionary of country counts by starting letter
print(country_counts)

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
import json

def get_first_ten_countries():
    with open('data/countries.js', 'r') as file:
        countries_data = json.load(file)
        first_ten_countries = countries_data[:10]
    return first_ten_countries

def get_last_ten_countries():
    with open('data/countries.js', 'r') as file:
        countries_data = json.load(file)
        last_ten_countries = countries_data[-10:]
    return last_ten_countries

# Example usage
first_ten = get_first_ten_countries()
last_ten = get_last_ten_countries()

print("First ten countries:", first_ten)
print("Last ten countries:", last_ten)

# Exercises: Level 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

# Sort countries by name, by capital, by population
# List of dictionaries representing countries
countries = [
    {'name': 'Finland', 'capital': 'Helsinki', 'population': 5540720},
    {'name': 'Sweden', 'capital': 'Stockholm', 'population': 10230185},
    {'name': 'Norway', 'capital': 'Oslo', 'population': 5391369},
    {'name': 'Denmark', 'capital': 'Copenhagen', 'population': 5818553},
    {'name': 'Iceland', 'capital': 'Reykjavik', 'population': 343399}
]

# Sort by name
sorted_by_name = sorted(countries, key=lambda x: x['name'])

# Sort by capital
sorted_by_capital = sorted(countries, key=lambda x: x['capital'])

# Sort by population
sorted_by_population = sorted(countries, key=lambda x: x['population'])

# Print the sorted lists
print("Sorted by name:")
for country in sorted_by_name:
    print(country)

print("\nSorted by capital:")
for country in sorted_by_capital:
    print(country)

print("\nSorted by population:")
for country in sorted_by_population:
    print(country)

# Sort out the ten most spoken languages by location.
# Example data representing languages spoken in different countries
languages_data = [
    {'language': 'English', 'location': 'USA', 'speakers': 360000000},
    {'language': 'Spanish', 'location': 'Mexico', 'speakers': 121000000},
    {'language': 'Chinese', 'location': 'China', 'speakers': 1191000000},
    {'language': 'Hindi', 'location': 'India', 'speakers': 341000000},
    {'language': 'Arabic', 'location': 'Egypt', 'speakers': 95000000},
    {'language': 'Portuguese', 'location': 'Brazil', 'speakers': 229000000},
    {'language': 'Bengali', 'location': 'Bangladesh', 'speakers': 158000000},
    {'language': 'Russian', 'location': 'Russia', 'speakers': 258000000},
    {'language': 'Japanese', 'location': 'Japan', 'speakers': 126000000},
    {'language': 'French', 'location': 'France', 'speakers': 77000000},
    # Add more language data as needed
]

# Sort languages by number of speakers in descending order
sorted_languages = sorted(languages_data, key=lambda x: x['speakers'], reverse=True)

# Extract the ten most spoken languages
ten_most_spoken_languages = sorted_languages[:10]

# Print the ten most spoken languages by location
for index, language in enumerate(ten_most_spoken_languages, start=1):
    print(f"{index}. {language['language']} - Spoken in {language['location']} by {language['speakers']} speakers")

# Sort out the ten most populated countries.
# Example data representing countries and their populations
countries_data = [
    {'name': 'China', 'population': 1444216107},
    {'name': 'India', 'population': 1393409038},
    {'name': 'United States', 'population': 332915073},
    {'name': 'Indonesia', 'population': 276361783},
    {'name': 'Pakistan', 'population': 225199937},
    {'name': 'Brazil', 'population': 213993437},
    {'name': 'Nigeria', 'population': 211400708},
    {'name': 'Bangladesh', 'population': 166303498},
    {'name': 'Russia', 'population': 145912025},
    {'name': 'Mexico', 'population': 130262216},
    {'name': 'Japan', 'population': 126050804},
    # Add more country data as needed
]

# Sort countries by population in descending order
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)

# Extract the ten most populated countries
ten_most_populated_countries = sorted_countries[:10]

# Print the ten most populated countries
for index, country in enumerate(ten_most_populated_countries, start=1):
    print(f"{index}. {country['name']} - Population: {country['population']}")