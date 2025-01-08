# This is lesson 18 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python For Loop

our_list_1 = [1, 1, 2, 3, 4]
for idx in range(len(our_list_1)):
    our_list_1[idx] = our_list_1[idx] + 1

print(our_list_1) # [2, 2, 3, 4, 5]

# There is a simpler way to write this
our_list_1 = [item + 1 for item in our_list_1]
print(*our_list_1) # 3, 3, 4, 5, 6

# These For-loops can also be used with other operators than + or add, for example multiplication
for idx in range(len(our_list_1)): our_list_1[idx] = our_list_1[idx] * 1000

print(*our_list_1) # 3000 3000 4000 5000 6000

# And this code runs on every item in the list and multiplies it with one thousand.
# For loops can be useful for many types of tasks, for example lists
list_animals = ['cat', 'dog', 'horse', 'bull', 'cow']
for animal in list_animals:
    print(animal)

print('')

# cat
# dog
# horse
# bull
# cow
# 

# For-loop can be used with Python's very powerful enumerate function to, for example, enumerate objects in a list
for idx, animal in enumerate(list_animals): print (idx, animal)

# 0 cat
# 1 dog
# 2 horse
# 3 bull
# 4 cow

# This can be a useful trick when creating a dictionary from a list, considering the need for unique keys to create the dictionary
# This is also useful for many data operations where enumerations are necessary.

# For-loops can be used on ranges or parts of lists or collections
# Use list slicing with for-loops
for animal in list_animals[0:2]: print(animal)

# cat
# dog

# Use ranges , the len() function, and step part of the range function and, for example, choose only every other animal in the list
for idx in range(1, len(list_animals), 2): print(list_animals[idx])

# dog
# bull
