# This is lesson 13 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python Tuples

# Python Tuples are a type of set (collection is probably a better word) 
# Ordered (indexable)
# Immutable
# Once it is created, it cannot be modified, but it can be transformed into a new tuple.

Tuple1 = (12345)
print(Tuple1) # 12345
print(type(Tuple1)) # <class 'int'>

Tuple1 = (12345, 1)
print(Tuple1) # (12345, 1)
print(type(Tuple1)) # <class 'tuple'>

Tuple1 = (12345, )
print(Tuple1) # (12345,)
print(type(Tuple1)) # <class 'tuple'>

# We can add more tuples
Tuple2 = ('hello', 'world')
Tuple3 = ('hello', 12345, 'world') # Tuples can hold arbitrary Python objects
Tuple4 = (1, 4, 2.73, 3.1) # Here we ad floats to a tuple of integers
print(Tuple2 + Tuple3) # ('hello', 'world', 'hello', 12345, 'world')
print(Tuple1 + Tuple4) # (12345, 1, 4, 2.73, 3.1)

# We can create nested Tuples or Tuples within Tuples and we can create Tuples incluiding, for example, name declared integers
# or floats, strings, etc.
Float1 = 3.91
Integer1 = 9
Tuple5 = (Float1, Integer1, ('hello', 'world'))
print(Tuple5) # (3.91, 9, ('hello', 'world'))
print(Tuple5[0]) # 3.91
print(Tuple5[1]) # 9
print(Tuple5[2]) # ('hello', 'world')

# We can access contents of a Tuple by referring to the order of items of object-items in the Tuple
print(Tuple3[0]) # hello
print(Tuple3[2]) # world

# Now we will use some advanced functions on our Tuples, and if you feel that this part of the video lecture is tough,
# complete the Python for Datahandling video course, and return to this part afterwards, if this part still feels tough,
# repeat the course once more, and return. You will feel that this code has become easy code for you to type and understand as
# well as develop your own.

# We will begin with the Length() or len() function for Tuples.
print(len(Tuple2)) # 2
print(len(Tuple4)) # 4

# As we can see, the printed numbers are 2 and 4, the number of items in the Tuples.

# Tuples can be accessed as 'ranges' using the : operator
print(Tuple4[0:2]) # (1, 4)

# We can loop Tuples, for example with for loops
for items in Tuple4:
    print(items)

# 1
# 4
# 2.73
# 3.1

# We can use the index positions, the len(), and loops to create functionality
for pos in range(len(Tuple3)):
    print(str(pos) + ' ' + str(Tuple3[pos]))

# 0 hello
# 1 12345
# 2 world    

# Tuple returns from functions, libraries and library functions is one of the main occurences of Tuples in current Python
# libraries.  The unchangeable property of Tuples is the main reason for using Tuples as a return item from a function or
# library.  Now we will look at unpacking, which is about unpacking variables from a Tuple, and presumably a return Tuple from
# a library.
Float2, Integer2, Tuple6 = Tuple5
print(str(Float2) + ' ' + str(Integer2) + ' ' + str(Tuple6)) # 3.91 9 ('hello', 'world')

# We can continue the unpacking further with Tuple6
String1, String2 = Tuple6
print(String1 + ' ' + String2) # hello world
