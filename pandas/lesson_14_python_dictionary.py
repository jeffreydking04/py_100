# This is lesson 14 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python Dictionary

Mailcat = {
    'Joe': 'joe@joe.gmail.com',
    'Anand': 'anand.anand@anand@aol.com',
    'Lisa': 'lisa@gmx.com'
}
print(Mailcat) # {'Joe': 'joe@joe.gmail.com', 'Anand': 'anand.anand@anand@aol.com', 'Lisa': 'lisa@gmx.com'}

# To add an instance 'Mohammed' to the dictionary, all we need to do is type:
Mailcat['Mohammed'] = 'mohammed@gmail.com'
print(Mailcat) # {'Joe': 'joe@joe.gmail.com', 'Anand': 'anand.anand@anand@aol.com', 'Lisa': 'lisa@gmx.com', 'Mohammed': 'mohammed@gmail.com'}

# As we can see from this code a dictionary is created with a name, the equality sign and two curly brackets.
# Name_of_dictionary = {} 
# We learned how to add another string instance to the dictionary.  Now we will add an integer key, string instance to the 
# Mailcat dictionary to show the versatility of a Python dictionary.
Mailcat[5] = 'This is a string value with an integer key.'
print(Mailcat) # {
#   'Joe': 'joe@joe.gmail.com', 
#   'Anand': 'anand.anand@anand@aol.com', 
#   'Lisa': 'lisa@gmx.com', 
#   'Mohammed': 'mohammed@gmail.com', 
#   5: 'This is a string value with an integer key.'
# }

# Now we will show some ways to address and print the Dictionary keys and items.
print(Mailcat.keys()) # dict_keys(['Joe', 'Anand', 'Lisa', 'Mohammed', 5])

print(Mailcat.values()) # dict_values(['joe@joe.gmail.com', 'anand.anand@anand@aol.com', 'lisa@gmx.com', 'mohammed@gmail.com', 'This is a string value with an integer key.'])

print(Mailcat.items()) # dict_items(
#       [
#           ('Joe', 'joe@joe.gmail.com'), 
#           ('Anand', 'anand.anand@anand@aol.com'), 
#           ('Lisa', 'lisa@gmx.com'), 
#           ('Mohammed', 'mohammed@gmail.com'),   
#           (5, 'This is a string value with an integer key.')
#       ]
#   )

# jk: notice it is a list of tuples

print(Mailcat['Lisa']) # lisa@gmx.com

print(Mailcat[5]) # This is a string value with an integer key.

print(Mailcat.get('Lisa')) # This will return the value for the key in the Dictionary, but if the value is not found a
# Default value will be returned (for example a None object.)
# lisa@gmx.com

# Note that key names must be correctly specified with UPPER-case characters or lower-case characters wherever appropriate.

# If we want to change the data value of a key in the Dictionary, we can make the change with this code:
Mailcat['Joe'] = 'joe2.joe2@gmail.com'
print(Mailcat['Joe']) # joe2.joe2@gmail.com

# To delete a key-value pair, it can be done with this code:
del Mailcat[5]
print(Mailcat) # {'Joe': 'joe2.joe2@gmail.com', 'Anand': 'anand.anand@anand@aol.com', 'Lisa': 'lisa@gmx.com', 'Mohammed': 'mohammed@gmail.com'}

# Now it is time for some more advanced Dictionary functions.  If they feel complex at this stage, return after completing the
# Python and Pandas sections.  If the following still feels complex, return again after completing the other parts of this 
# video course–all will be clear with some practice and that exercise makes the master or mastery.

# We will start with the len().  This function tells us the number of key-value pairs in a Dictionary, or the number of items,
# elements, or key-value instances in the Dictionary.

print(len(Mailcat)) # 4

# str() function creates a string of our Dictionary.  This may be useful in some Text Mining applications.
print(str(Mailcat)) # return and print the Mailcat Dictionary as a single string within curly brackets.
# {'Joe': 'joe2.joe2@gmail.com', 'Anand': 'anand.anand@anand@aol.com', 'Lisa': 'lisa@gmx.com', 'Mohammed': 'mohammed@gmail.com'}

# Now we will show some loops, and this loop iterates through all the keys in a dictionary and prints each key on
# a new line
for m in Mailcat:
    print(m)

# Joe
# Anand
# Lisa
# Mohammed

# This more advanced loop iterates through all key value pairs in our Dictionary and prints each key-value on a new line
for k, v in Mailcat.items():
    print(k, v)

# Joe joe2.joe2@gmail.com
# Anand anand.anand@anand@aol.com
# Lisa lisa@gmx.com
# Mohammed mohammed@gmail.com

Mailcat.clear() # This code deletes all elements in our Dictionary.
print(Mailcat) # {}

# Now we will show how to delete the Dictionary
del Mailcat
# print(Mailcat) # NameError: name 'Mailcat' is not defined
