# This is lesson 19 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python List Comprehension for Data Handling

# new_list = [expression for element in iterable]

# We can create other data structures using list comprehensions.  The following is still a list comprehension, even though the result is a dictionary.
example = {
    'one': 1,
    'two': 2,
}
example_times_10 = {
    k: v * 10 for k, v in example.items()
}

print(example.items()) # dict_items([('one', 1), ('two', 2)])
print(example_times_10.items()) # dict_items([('one', 10), ('two', 20)])

# This is because items() returns a list, meaning we are iterating over a list to create the structure.

# Type some code

# List Comprehensions vs. For-Loops
a_list = [4, 5, 6, 7, 8]
print(a_list) # [4, 5, 6, 7, 8]

# Show the for-loops 3 lines/rows of code vs. the List Comprehension 1 line/row
b_list = []
for element in a_list:
    b_list.append(element + 1)

print(b_list) # [5, 6, 7, 8, 9]

a_list_plus_1 = [element + 1 for element in a_list]
print(a_list_plus_1) # [5, 6, 7, 8, 9]

# This is the optimal setting for making use of List Comprehensions.  It removes about 50-66% of the code and for small lists
# which in RAM memory, list comprehensions increase code execution speed with about 100%.

# List Comprehensions for multiple dimensions may quickly grow in complexity.
# Let's take a look at 2D list comprehensions.
list_of_lists = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10],
]
print(list_of_lists)

# [
#     [2, 3, 4],
#     [5, 6, 7],
#     [8, 9, 10]
# ]

list_of_lists_minus_1 = []
for l in list_of_lists:
    c_list = []
    for el in l:
        c_list.append(el - 1)
    list_of_lists_minus_1.append(c_list)

print(list_of_lists_minus_1) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Let's show the proper way to type 2D list comprehensions
list_of_lists_2 = [[element + 1 for element in l] for l in list_of_lists]
print(list_of_lists_2) # [[3, 4, 5], [6, 7, 8], [9, 10, 11]]

# This 2D example shows how powerful and useful list comprehensions are when used properly in 2D. 2D is however considered the generally
# highest dimension where list comprehensions remain Pythonic also for non-trivial examples such  as element increase one or decrease one.
# Let's take a look at 3D lists and 3D list comprehensions.
list_3D = [
    [
        [1, 2], 
        [3, 4],
    ],
    [
        [5, 6], 
        [7, 8],
    ],
]
print(list_3D) # [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

list_3D_minus_1 = []
for l in list_3D:
    d_list = []
    for lst in l:
        e_list = []
        for el in lst:
            e_list.append(el - 1)
        d_list.append(e_list)
    list_3D_minus_1.append(d_list)
print(list_3D_minus_1) # [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]

# 3D proper list comprehension
list_3D_plus_1 = [[[element + 1 for element in lst] for lst in l] for l in list_3D]
print(list_3D_plus_1) # [[[2, 3], [4, 5]], [[6, 7], [8, 9]]]

# As you can see in this case, the 3D list comprehension is good but a tad bit complex even for simple + 1 additions. Not following
# the strict naming scheme which is implemented above may result in readability issues for mare complex expressions, ambitious, or nasty naming
# schemes, or using a list/element scheme different from the visit all lists/elements once approach used above.  These readability issues may
# create 'seniority', or 'non-pythonic' code.
# The general recommendation is to stay in 2D because 99% of all coders, with certainty understand 2D code.
