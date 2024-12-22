# Python Strings

# Let's start with creating the example_string and print it to the screen

example_string = 'hello world' # A string is created using assignment
print(example_string)

# Print the object type or class of the string object
print(type(example_string)) # <class 'str'>

# Let's add to strings together to create a new string through assignment
example_string2 = "again"
example_string3 = example_string + example_string2
print(example_string3) # hello worldagain

example_string3 = example_string + ", " + example_string2
print(example_string3) # hello world, again

# Let's take a look a the iterable property of Python Strings.  We will take a look at the parts of a string using a loop.
for x in range(len(example_string3)):
    print(example_string3[x])

# Let's turn the output to one line
example_string3a = ""
for x in range(len(example_string3)):
    example_string3a = example_string3a +  " " + example_string3[x]
print(example_string3a) # h e l l o   w o r l d ,   a g a i n

# Let's study this string a bit deeper...
example_string4 = "" # Create an empty string object
for x in range(len(example_string3)):
    example_string4 = example_string4 + example_string3[x]
    print(example_string4 + " " + str(len(example_string4)))

# And we can make some changes to the code
for c in range(len(example_string3)):
    print(example_string3[:c + 1] + " " + str(len(example_string3[:c + 1])))

# Let's print the text backwards
for e in range(len(example_string3)):
    print(example_string3[e:] + " " + str(len(example_string3)))

# Let's take a brief look at element based access in string through the Indexing method
# Printing example_string3
print(example_string3) # hello world, again

# Make selections from example_string3 usingi the Indexing method
example_string5 = example_string3[1] + example_string3[13] + example_string3[8]
print(example_string5) # ear
