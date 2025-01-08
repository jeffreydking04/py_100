# This is lesson 15 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python List

Ourfirstlist = [7, 4, 3, 9, 'bananas']
print(str(Ourfirstlist[3]) + str(Ourfirstlist[2]) + ' ' + str(Ourfirstlist[4])) # 93 bananas
# str(list[index]) instructs Python to read the ints as strings. This is one basic type of control of list output.

# A list may be changed by assigment
Ourfirstlist[1] = 2
print (Ourfirstlist) # [7, 2, 3, 9, 'bananas']

# New items may be added with the append() method/function.
Ourfirstlist.append('apples')
print(Ourfirstlist) # [7, 2, 3, 9, 'bananas', 'apples']

# There are two main functions or methods for removing items/objects from a list, the del statement and the remove() method:
del Ourfirstlist[4] # Remove by index
print(Ourfirstlist) # [7, 2, 3, 9, 'apples']
Ourfirstlist.remove('apples') # Remove by value
print(Ourfirstlist) # [7, 2, 3, 9]

# jk: How about this:
jk_list = [1, 2, 1]
jk_list.remove(1)
print(jk_list) # [2, 1]  Only the first found incident

# Python lists can be added together using either the + operator or the extend or append functions or methods:
Oursecondlist = [1, 4, 5, 6, 8]
Ourthirdlist = Ourfirstlist + Oursecondlist
print(Ourthirdlist) # [7, 2, 3, 9, 1, 4, 5, 6, 8]
Ourfirstlist.append(Ourthirdlist)
print(Ourfirstlist) # [7, 2, 3, 9, [7, 2, 3, 9, 1, 4, 5, 6, 8]]
Ourthirdlist.extend(Oursecondlist)
print(Ourthirdlist) # [7, 2, 3, 9, 1, 4, 5, 6, 8, 1, 4, 5, 6, 8]
print(len(Ourthirdlist)) # 14
print(len(Ourfirstlist)) # 5

# jk: + and extend adds each element of each list to a new list
# jk: append adds whatever argument you supply to the list as a single element

# Sort our third list
print(Ourthirdlist) # [7, 2, 3, 9, 1, 4, 5, 6, 8, 1, 4, 5, 6, 8]
Ourthirdlist.sort()
print(Ourthirdlist) # [1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9]
Ourthirdlist.sort(reverse=True)
print(Ourthirdlist) # [9, 8, 8, 7, 6, 6, 5, 5, 4, 4, 3, 2, 1, 1]
Ourthirdlist.sort()

# Address ranges of the list
print(Ourthirdlist[1:4]) # [1, 2, 3]
print(Ourthirdlist[:3]) # [1, 1, 2]
print(Ourthirdlist[12:]) # [8, 9]

# Move objects from one list to another list with the .pop() function
Ourthirdlist.append(Ourfirstlist.pop(1))
print(Ourthirdlist) # [1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 2]  2 was popped off of 1 to the end of 3
print(Ourfirstlist) # 

# jk: Let's make that more clear what pop is doing:
print(jk_list) # [2, 1]
jk_list_2 = [5, 7]
jk_list_2.append(jk_list.pop(0))
print(jk_list) # [1] # pop(0) removed the element in place
print(jk_list_2) # [5, 7, 2]

# Move objects from one list to a specified position of another list using the .insert() and .pop() functions
# jk: Doing this with my lists because his lists are too many numbers to easily keep track of:
jk_list_2.insert(1, jk_list.pop(0))
print(jk_list_2) # [5, 1, 7, 2]
print(jk_list) # []

# Use Python native functions type() or isinstance() to check object types if you don't control list input or list contents.
# It is a good practice to always do this in real application code. Let's show basic functions for this with the assumption
# of having a list with only integers or wanting such a list with integer contents.  Basic functions only.
str_test1 = '1'
str_test2 = 1
Ourfourthlist = []
Ourfourthlist.append(str_test1)
print(Ourfourthlist) # ['1']
if type(Ourfourthlist[-1]) is not int:
    print('The object is not an integer.')
    del Ourfourthlist[-1]
else:
    print('The object is an integer.')

print(Ourfourthlist) # []

if isinstance(str_test2, int):
    Ourfourthlist.append(str_test2)

print(Ourfourthlist) # [1]
