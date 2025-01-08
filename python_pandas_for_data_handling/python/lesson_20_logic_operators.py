# This is lesson 20 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python Logic Operatiors and Conditional Code Branching

list_3 = [3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 9, 10, 10, 11]
for idx in range(len(list_3)):
    list_3[idx] = list_3[idx] * 1000

print(list_3) # [3000, 3000, 4000, 5000, 6000, 6000, 7000, 7000, 8000, 8000, 9000, 10000, 10000, 11000]

list_4 = [] # We create our list_4
for idx in range(len(list_3)):
    if list_3[idx] >= 7000:
        list_4.append('High')
    elif ((list_3[idx] >= 5000) and (list_3[idx] < 7000)):
        list_4.append('Medium')
    else:
        list_4.append('Low')

print(list_4) # ['Low', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High']

# We can print the result into a table using another loop (note that in this example both lists have the same length)
for idx in range(len(list_3)):
    print(str(list_3[idx]) + '\t' + str(list_4[idx]))

# 3000    Low
# 3000    Low
# 4000    Low
# 5000    Medium
# 6000    Medium
# 6000    Medium
# 7000    High
# 7000    High
# 8000    High
# 8000    High
# 9000    High
# 10000   High
# 10000   High
# 11000   High

# Some basic descriptive statistics
list_unique_categories = []
no_operation_counter = 0
for item in list_4:
    if item not in list_unique_categories:
        list_unique_categories.append(item)
        print(item + ' number in category: ' + str(list_4.count(item))) 
    else:
        no_operation_counter = no_operation_counter + 1

print(list_unique_categories)
print(no_operation_counter)

# Low number in category: 3
# Medium number in category: 3
# High number in category: 8
# ['Low', 'Medium', 'High']
# 11

# A dictionary version of this
desc_statistics = {}

for word in list_4:
    if word in desc_statistics:
        desc_statistics[word] += 1
    else:
        desc_statistics[word] = 1

# print a sorted output
for word in sorted(desc_statistics, key=desc_statistics.get):
    print(desc_statistics[word], word)

# 3 Low
# 3 Medium
# 8 High
