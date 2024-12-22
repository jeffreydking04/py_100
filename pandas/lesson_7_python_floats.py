# Lesson from Henrick Johansson's Master Pandas and Python for Data Handling

# Lesson 7: Python Floats

# Create a Python Float using with assignment
real_num = 5.3 # real_num equals 5.3. A Python Float is created through assignment.
print(real_num) # 5.3
print(type(real_num)) # <class 'float'>

# Create more Floats and combine them together to create new Floats through assignment.
fp_two = 3.2 # Float value
print(fp_two) # 3.2

# Try Addition
fp_three = fp_two + real_num # A Float value plus a Float value is a Float value.
print(fp_three)  # 8.5

# Try Subtraction
fp_four = real_num - fp_two # A Float valu minus a Float value is a Float value.
print(fp_four) # 5.3 - 3.2 = 2.1 ..... or?
# Actual result 2.09999999999...6

# Round the result
print(round(fp_four, 1)) # 2.1

# This issue is caused by the 64 bit floatting points inability to store certain numbers exactly.

# Try multiplication
fp_four_b = round(fp_four, 1)
fp_five = fp_four * fp_two # A Float value multiplied with a Float value is a Float value
fp_five_b = fp_four_b * fp_two
print(fp_five) # 6.719999...
print(fp_five_b) # 6.720000...1

# Which one is correct
# Both numbers become the same number when properly rounded according to the rules of mathematics and measurements... round(fp_five, 2)
# round(fp_five, 2) is the rule of 'math' and 'measurements' way.
# round(fp_five_b, 2) most often happens in practice, and combined with floating points is a contributing cause to
# spacerockets and aircraft crashes
# Missiles missing targets and measurement errors in general. However for 64bit floating points or bigger sizes of floating points...
# These rounding errors are most often negligable for any ordinary applications.
# This statement is not necessarily true for 8, 16, or 32 bit floating points.
# However, as Python uses 64bit floating points as the least sizeable floating ppoint this issue will only affect Python applications
# in certain highly unusual ways which we will show a bit later.

# Try Division
fp_six = fp_three / fp_two # A Float value divide with a Float value is a Float value.
print(fp_six) # 2.65625

# Floats are used in many calculations. Let's create a trivial badass example of a floating point equation which goes bad:
res = 1.0 # floats are in this example initialized at 1.0 for use with multiplication
res_b = 1.0
for x in range(1,6):
    res = res * x * fp_four
    res_b = res_b * x * fp_four_b
    print(x * fp_four)
    print(x * fp_four_b)
    print(res)
    print(res_b)
    print(res - res_b)

# jk: As we iterate through this the final print is how the expected value diverges rapidly from the 'incorrect' method.
# jk: The rule is round at each step to the appropriate decimal place to get the mathematically correct result.

# Increase the size of the Floats through the loop to visualize the differences due to the round function and this setup...

res = 1.0 # floats are in this example initialized at 1.0 for use with multiplication
res_b = 1.0
for x in range(1,66):
    res = res * x * fp_four
    res_b = res_b * x * fp_four_b
    print(x * fp_four)
    print(x * fp_four_b)
    print(res)
    print(res_b)
    print(res - res_b)

# jk: In the end, the error is astronomical. -9.5...e+97

# Increase the size of the floats even more through the loop to show what can happen over time...

res = 1.0 # floats are in this example initialized at 1.0 for use with multiplication
res_b = 1.0
for x in range(1,666):
    res = res * x * fp_four
    res_b = res_b * x * fp_four_b
    print(x)
    print(x * fp_four)
    print(x * fp_four_b)
    print(res)
    print(res_b)
    print(res - res_b)

# jk: Overflow error because the error is outside the range of floating points.
# jk: res and res_b are then treated as inf (infinity) and res - res_b is thus inf - inf which is nan

# Intriguing
# Conclusions: If the floating point unit or code cannot properly define a number, rounding that improperly defined number will not change
# this fact when using that rounded approximated number in calculations as 2.099999.... -> 2.1 will be returned to 2.099999.... even when using
# round(2.099999..., 1), the next time 2.1 is sent to the floating point definition and circuitry.
# This is a property of the floating-point definitions and circuitry.
# The grave danger is when something in the calculation creates a permanent difference between rounded floating points and floating points
# and this is what we created in this artificial badass (sic) example.

# Let's take a brief look at casting or converting other Python datatypes to Python Floats:
fp_seven = float(5) # Cast the int 5 to a float 5.0
fp_eight = float('3.3') # Cast the string '3.3' to a float 3.3
jk_one = float('3') # Just checking because remember int('3.3') doesn't work even though Python can cast strings and floats to ints
print(fp_seven) # 5.0
print(type(fp_seven)) # <class 'float'>
print(fp_eight) # 3.3
print(type(fp_eight)) # <class 'float'>
print(jk_one) # 3.0
print(type(jk_one)) # <class 'float'>

# Let's try to convert a 'suitable' Python Float to a Python Tuple with two Python ints.
fp_nine = 0.5 # 0.5 = 1/2
ratio_tuple = fp_nine.as_integer_ratio()
print(ratio_tuple) # (1, 2)
print(str(ratio_tuple[0]) + '/' + str(ratio_tuple[1])) # 1/2

# jk: He is confident we know enough about floats now.  rofl.
# jk: Really loved this hour with floats.  Usually floats are taught as a decimal in about 2 seconds.
