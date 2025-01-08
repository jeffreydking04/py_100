# This is lesson 6 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python Integers

# Create our first Python Integer
whole_num = 5 # whole_num = 5. This Python Integer through assignment.
print(whole_num) # 5

# Create more integers and add them together to create new integers through assignment
num_two = 3 # Intgeger Value
num_three = num_two + whole_num # Integer value plus an Integer value is an Integer value.
print(num_three) # 8

# Test Subtraction, Multiplication, and Division
# Subtraction
num_four = whole_num - num_two # An Integer value minus an Integer value is an Integer value.
print(num_four) # 2

# Multiplication
num_five = num_four * num_three # An Integer value multiplied by an Integer value is an Integer value.
print(num_five) # 16

# Division
num_six = num_five / whole_num # Two Integer values divided with each other returns a float if a single division sign is used.
print(num_six) # 16 / 5 or 3.2

# Type Checking
print(type(num_five)) # <class 'int'>
print(type(num_six)) # <class 'float'>

# Floor Division
num_seven = num_five // whole_num # Two Integer values floor divided with each other returns/creates a rounded Integer
print(num_seven) # 3
print(type(num_seven)) # <class 'int'>

# Integers can be used to keep track of Python loops
for x in range(1, 6): # range(x, y) is inclusive of x, exclusive of y
    print(x)

# 1
# 2
# 3
# 4
# 5

# Other data types can be converted or cast as Integers  *if* the data type's value is 'suitable'.
num_eight = int(5.5) # Cast a float 5.5 as an Integer with the value 5.
num_nine = int('3') # Cast the string '3' as an Integer with the value 3.
print(num_eight) # 5
print(type(num_eight)) # <class 'int'>
print(num_nine) # 3 
print(type(num_nine)) # <class 'int'>

# Bonus material from jk:
# It is tempting to think that because Python recognizes int(5.5) and int('5'),
# that it will correctly recognize int('5.5'), but it produces an error.
# num_ten = int('5.5') # ValueError: invalid literal for int() with base 10: '5.5'

# As we are sure to see in Lesson 7: Python Floats, the following is valid syntax: 
num_ten = float('5.5') # Cast a string '5.5' as a Float with the value 5.5.
print(num_ten) # 5.5
print(type(num_ten)) # <class 'float'> 
