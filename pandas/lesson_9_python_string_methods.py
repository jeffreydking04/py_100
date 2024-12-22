# This is lesson 9 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python String Methods

# Some Python String Object Methods

# Create some example strings
e_str1 = 'he11o' # This string is intentionally misspelled in a strange fashion
e_str2 = 'WORLD' # string 2 uses uppercase letters
e_str3 = ', again' # only uses lowercase letters
e_str4 = '123.3' # a float as a string
e_str5 = '32' # an integer as a string
e_str6 = 'hello world, again' # an ordinary string example
e_str7 = '   hello    ' # 'hello' with added whitespace before and after the visible string
e_str8 = '  world,  ' # and this is the string 'world,' with added whitespace before and after the visible string

# Let's begin with some tests on the strings
print(e_str4.isalpha()) # False
print(e_str4.isdecimal()) # False
print(e_str4.isnumeric()) # False
print(e_str5.isnumeric()) # True

# jk: isdecimal() just checks if all the characters are numbers; how does it differ from isnumeric()

print(e_str2.isupper()) # True
print(e_str1.isupper()) # False
print(e_str3.islower()) # True

# Methods for searching for content inside strings. The methods return integer values descirbing the positions (jk: indices) of findings
# and -1 if no findings occur.

print(e_str6)
print(e_str6.find('world')) # Returns the position of the first finding's first element
print(e_str6.rfind('lo')) # Returns the last occurance's first element
print(e_str6.find('aircraft')) # No occurence and returns -1

# Methods can count the occurences of a substring; a string inside a string and it is important to remember that while a string is
# a word, a string can also be a sentence, paragraph, book, or an entire library, or even more...
print(e_str6.count('l')) # 3

# Some methods can change or replace the contents of a string or create a new copy of the 'trasformed' string
print(e_str1.capitalize()) # He11o 
print(e_str2.lower()) # world
print(e_str3.upper()) # , AGAIN
print(e_str6.replace('l', '1')) # he11o wor1d, again

# A method that can split strings into a list of strings
e_str10 = e_str7 + e_str8 # Creates a new string
print(e_str10) # '   hello   world,   '
list_strings = e_str10.split() # Splits e_str10 into parts
print(list_strings) # ['hello', 'world,']
for string in list_strings:
    print(string)

# Methods can be used to modify new string copies, for example by removing whitespace
print(e_str10) # Display e_str10 with whitespace, e_str10 = e_str7 + e_str_8  => '  hello    world,    '
print(e_str7.lstrip() + e_str8.rstrip()) # => 'hello    world,'
print(e_str7.strip() + ' ' + e_str8.strip()) # Double sided strip for both strings + new whitespace  => 'hello world,'
print(e_str10.strip()) # Double sided whitespace removal for e_str10 => 'hello    world'

# The applications and usefulness of string functions are near limitless...
