# This is lesson 22 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python Functions

list_3 = [3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 9, 10, 10, 11]
for idx in range(len(list_3)):
    list_3[idx] = list_3[idx] * 1000

print(list_3) # [3000, 3000, 4000, 5000, 6000, 7000, 7000, 8000, 8000, 9000, 10000, 10000, 11000]

def calc_mean(lst = []):
    sum = 0.0
    for idx in range(len(lst)):
        sum += lst[idx]

    our_mean = sum/len(lst)
    return our_mean

# We can use the function like this:
our_mean = calc_mean(list_3)
print(our_mean) # 6928.57...

def calc_mean_2(lst = []):
    if lst is None:
        our_mean_2 = 0.
    sum = 0.0
    if len(lst) == 0:
        our_mean_2 = 0.0
    else:
        for idx in range(len(lst)):
            sum += lst[idx]
        our_mean_2 = sum / len(lst)
    return our_mean_2

# We can now use this function much more safely
our_mean_2 = calc_mean_2(list_3)
print(our_mean_2) # 6928.57...

# Let's make more a more general function and count the number of unique items in a one-dimensional list or other list-similar
# collection.
def count_unique_items(collection):
    desc_stats = {} # This is a dictionary and the return item
    for item in collection:
        if item in desc_stats:
            desc_stats[item] += 1
        else:
            desc_stats[item] = 1
    return desc_stats

# We can use this function in many ways.
# We can call it as part of another function without explicitly naming or referncing the return object
print(count_unique_items(list_3)) # {3000: 2, 4000: 1, 5000: 1, 6000: 2, 7000: 2, 8000: 2, 9000: 1, 10000: 2, 11000: 1}

# We can name the return object, sort and print the output of the function
desc_statistics_2 = count_unique_items(list_3)
for word in sorted(desc_statistics_2, key=desc_statistics_2.get):
    print((desc_statistics_2[word], word))

# (1, 4000)
# (1, 5000)
# (1, 9000)
# (1, 11000)
# (2, 3000)
# (2, 6000)
# (2, 7000)
# (2, 8000)
# (2, 10000)

# We can make an even more general function able to handle uneven multi-type 2D list of lists. We can show how functions
# Are able to reuse code and lessen the number of lines of code necessary for a program.
# Creat a spectial 2D uneven multi-type list of lists.
special_list = [
    [
        1,
        3,
        'nine',
    ],
    [
        2.32,
        3,
        'nine',
        'nine',
    ],
    [
        1,
        4,
        4,
        3,
        'six',
    ],
]

print(special_list) # [[1, 3, 'nine'], [2.32, 3, 'nine', 'nine'], [1, 4, 4, 3, 'six']]

# Create a standard function for adding dictionaries 'together'
def add(dictionary_a, dictionary_b):
    return_dict = {key: dictionary_a.get(key, 0) + dictionary_b.get(key, 0) for key in set(dictionary_a) | set(dictionary_b)}
    return return_dict

# Create a function creating dictionaries from the list/collection and use our add function to add them together.
def count_unique_items_2(collection):
    dict_unique_items = {} # Dictionary and return item
    for item in collection:
        dict_item = count_unique_items(item)
        dict_unique_items = add(dict_unique_items, dict_item)
    return dict_unique_items

descriptive_stats = count_unique_items_2(special_list)
for word in sorted(descriptive_stats, key=descriptive_stats.get):
    print((descriptive_stats[word], word))

# (1, 2.32)
# (1, 'six')
# (2, 1)
# (2, 4)
# (3, 3)
# (3, 'nine')
