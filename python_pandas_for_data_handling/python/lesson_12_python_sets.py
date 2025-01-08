# This is lesson 12 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python Sets

# Sets are a native Python data structure, as opposed to Pandas data frames, which are part of
# the Pandas library, and thus not 'native'.

# Sets are an unordered collection of unique objects.  Elements are in or they are out.
# Sets are mutable, but can be frozen using frozenset().

# Because they are unordered, they are not indexed.

# But this does not mean that the ordering is random or arbitrary.????

# Is economical with regard to memory, but as memory becomes cheap, more sophisticated data structures become better options.

# 'It is alleged that Python sets are actually dictionaries under the hood.'  jk: I paraphrased, but that is an awesome sentence
# jk: particularly the use of the word alleged.  Very clandestine, nefarious undertones.

# 'So start up your code editors, because we are going to type some code.'  jk: It is hilarious that he says this on every lesson
# and my Pavlovian response at this point is to get excited to be 'typing some code'.

# Python Set

# Create a set named fruits with named fruit objects (strings) inside the set
fruits = {'banana', 'apple', 'orange', 'apple', 'peach', 'banana'}
print(fruits) # {'banana', 'peach', 'orange', 'apple'}
print(type(fruits)) # <class 'set'>

# All duplicates of fruits were automatically removed from the set and only one instance of each fruit object remains
# the objects appear to be random or unordered, but are they random?

fruits_2 = {'banana', 'apple', 'orange', 'apple', 'peach', 'banana'}
print(fruits_2) 

# jk: Everytime I run this, both fruits and fruits_2 print in the same order, but not the same as the previous time I ran it.
# jk: His output is different between running too, but he concludes that this shows it is not random.  I do not understand.

# The Python Set is unordered not 'random' - there is an order to the set under the 'hood'...

# Add more fruits to the fruits set with the add function
fruits.add('lemon')
fruits.add('banana')
print(fruits) # {'apple', 'peach', 'banana', 'orange', 'lemon'} This shows that duplicates are removed and that new items are added.

# Add multiple objects/itmes to a set with the update function/method...
fruits.update(['pear', 'citrus', 'peach']) # jk: update with a List???
print(fruits) # {'citrus', 'orange', 'lemon', 'peach', 'banana', 'apple', 'pear'}

# The new fruits were added and the duplicates were removed.

# Sets can be copied using the copy function
fruitage = fruits.copy() # This will create a shallow copy
print(fruitage) # {'banana', 'apple', 'citrus', 'peach', 'lemon', 'orange', 'pear'}

# jk: Let's explore the shallowness of this:
# a_list = [1, 2]
# a_set = {3, 4, a_list} 
# print(a_set) # TypeError: unhashable type: 'list'

# jk: My first thought is that more complicated data structures that would change behavior based on shallow or deep copying
# jk: can't be elements of a set in the first place, but perhaps I am being naive.

# Remove objects from a set using the remove() function/method
fruitage.remove('citrus')
print(fruitage) # {'orange', 'apple', 'lemon', 'banana', 'peach', 'pear'}
print('test fruits') # test_fruits
print(fruits) # {'citrus', 'orange', 'pear', 'banana', 'lemon', 'peach', 'apple'}

# A shallow copy is sufficient for this use... the alternative is a deepcopy()

# Clear a set from its objects using the clear function/method
fruits.clear()
print(fruits) # set()

# The fruits set is empty

# Delete a set with the delete() function
del fruits
# print(fruits) # This code will throw an error if fruits have been deleted

# NameError: name 'fruits' is not defined

# Loop through a set using a for loop and print the contents
for fruit in fruitage:
    print(fruit)
# banana
# peach
# orange
# apple
# lemon
# pear

# Create an empty basket set and put some fruit in it using set math operations and a 'mover' set
mover_set = {'apple', 'peach', 'banana'}
print(fruitage) # {'apple', 'banana', 'orange', 'pear', 'peach', 'lemon'}
basket = mover_set.intersection(fruitage)
fruitage.difference_update(basket) # Future Python sets may have a one-liner method for moving an object between two sets
print(basket) # {'apple', 'peach', 'banana'}
print(fruitage) # {'orange', 'pear', 'lemon'}

# jk: It is weird that he says that the mover_set was 'moved' to the basket set.
# jk: Nothing was moved.  A new set was defined and then those items were removed from the old set.
# jk: So I get why he says that, but that is not what happened in the code.
# jk: You have two sets with an intersection and you want to define this as three sets,
# jk: the outer of each and the intersection, so you 'move' the intersection to a new set
# jk: by first defining the new set as the intersection, then removing the intersection from the other sets

set_1 = {1, 2, 3, 4} 
set_2 = {3, 4, 5, 6} 
set_3 = set_1.intersection(set_2)
set_1.difference_update(set_3)
set_2.difference_update(set_3)
print(set_1) # {1, 2}
print(set_2) # {5, 6}
print(set_3) # {3, 4}

# jk: That is pretty neat, actualy and I can see why you might want a one liner to do that:
def move_intersection(set_1, set_2):
    set_3 = set_1.intersection(set_2)
    set_1.difference_update(set_3)
    set_2.difference_update(set_3)
    return set_3

s_1 = {1, 2, 3, 4} 
s_2 = {3, 4, 5, 6} 
s_3 = move_intersection(s_1, s_2)
print(s_1) # {1, 2}
print(s_2) # {5, 6}
print(s_3) # {3, 4}

# jk: The end result is that you have effectively removed the intersection from the existing sets and placed it (moved it) in a new set

# jk: He doesn't talk about some of the constraints of the elements of sets (i.e. unhashable objects and why that is a constraint)
