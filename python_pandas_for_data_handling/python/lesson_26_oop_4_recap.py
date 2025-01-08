# This is lesson 26 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python Object Oriented Programming IV:  Recap and More

# This is the last Python for Data Handling lecture.  From here we get into Pandas and I am here for it.

# Create a dictionary of lists where the lists have names as keys and lists as values
# Var_dict = {
#     'Birth_date': ['1992/11/09', '1987/02/13', '1999/05/02', '2003/08/03',],
#     'E_start_date': ['2022-04-23', '2022-07-12', '2021-12-21', '2023-02-21',],
#     'E_end_date': ['2022-09-17', '2023-01-09', '2022-07-01', '2023-08-01',],
#     'W_start_date': [221, 198, 178, 184,],
#     'W_end_date': [208, 191, 176, 179,],
# }

# Create a hearder for .txt file
# file_header = ''
# for k in Var_dict:
#     file_header += str(k) + ' '
# file_header += '\n'
# print(file_header)

# Create and print Text_file.txt file
# with open('pandas/text_file.txt', 'w') as file:
#     file.write(file_header)
# file.close()

# Turn our dictionary of lists into a list of lists and transpose it to a list of lists
# Var_list = list(Var_dict.values())
# Var_list_t = [[row[i] for row in Var_list] for i in range(len(Var_list[0]))]
# print(Var_list)
# print(Var_list_t)

# Open Text_file.txt and print our data values to the .txt file
# print_string = ''
# with open('pandas/Text_file.txt', 'a') as file:
#     for v in Var_list_t:
#         for var in v:
#             print_string += str(var) + ' '
#         print(print_string)
#         print_string += '\n'
#         file.writelines(print_string)
#         print_string = ''
# file.close()


# Lecture begins; before was preamble
# Import datetime module as dt and matplotlib as plt
import datetime as dt
import matplotlib.pyplot as plt

# Read a text_file.txt into a read_datas list of strings. The file can be downloaded from the course page or 
# be created with a downloadable .py file.   This read .txt can be adapted to almost any type of textbaseed data file.
# And the .py file is interesting to study of its advanced data handling code.

read_datas = []
read_counter = 0
with open('pandas/text_file.txt') as input_file:
    for read_data in input_file:
        read_datas.append(read_data)
        read_counter += 1

input_file.close()

# print(read_counter)
# print(read_datas[0]) # print the header
# print(read_datas)

# Use a function to split our list of strings into lists. Split on whitespace
def split_data(lst=[]):
    hder = []
    bd = []
    esd = []
    eed = []
    wsd = []
    wed = []
    newline = []
    for data in lst:
        if read_datas.index(data) == 0: # this is special treatment for the header
            hder = data.split(' ')
            del hder[-1] # Delete the newline at the last position of the header list
        else:
            words = data.split(' ')
            bd.append(words[0])
            esd.append(words[1])
            eed.append(words[2])
            wsd.append(words[3])
            wed.append(words[4])
            newline.append(words[5])
    
    del newline # the newline is a feature of the .txt file, and it is used in the textfile to structure data
    return hder, bd, esd, eed, wsd, wed

# Use our function to create a list of headers and 5 lists of read variables (in lists)
Header, Birth_date, E_start_date, E_end_date, W_start_date, W_end_date = split_data(read_datas)

# Print the variables to check that everything executed properly
# print(Header)
# print(Birth_date)
# print(E_start_date)
# print(E_end_date)
# print(W_start_date)
# print(W_end_date)

# Let's convert the data to usable formats. Header is string data, Birth_date should be converted to DateTime,
# E_start_date and E_end_date are strings directly compatible with DateTime.  W_start_date and W_end_date are strings
# directly convertible to Integer format.  We will create DateTime objects from strings to integers.
for idx in range(len(Birth_date)):
    Birth_date[idx] = dt.datetime.strptime(Birth_date[idx], '%Y/%m/%d')
    E_start_date[idx] = dt.datetime.strptime(E_start_date[idx], '%Y-%m-%d')
    E_end_date[idx] = dt.datetime.strptime(E_end_date[idx], '%Y-%m-%d')
    W_start_date[idx] = int(W_start_date[idx])
    W_end_date[idx] = int(W_end_date[idx])


# print(Birth_date[0]) # This is an interesting feature of DateTime objects and lists.
# print(E_start_date)
# print(E_end_date)
# print(W_start_date)
# print(W_end_date)

# Inside a list, the Date Time object looks like: datetime.datetime(2022, 4, 23, 0, 0)
# Outside a list: 1992-11-09 00:00:00

# We will calculate more variables with practical use
E_duration_days = []
Age_at_E_years = []
Zero_list = []
E_labels = []
for idx in range(len(Birth_date)):
    E_duration_days.append((E_end_date[idx] - E_start_date[idx]).days)
    Age_at_E_days = E_end_date[idx] - Birth_date[idx]
    Age_at_E_years.append(Age_at_E_days.days//365)
    Zero_list.append(0)
    E_labels.append('E_' + str(idx + 1))

# print(E_duration_days)
# print(Age_at_E_years)
# print(E_labels)

# We have a list Header with a variable containing the names of the base variables.  And we have a dataset of five lists with
# base variables named Birth_date, E_start_date, E_end_date, W_start_date, W_end_date.  We have four lists with calculated or 
# created variables. In total, we have 10 lists and 9 of these lists can be said to form a 'virtual spreadsheet' or columns
# linked to each other through the order of the data elements in the lists.
# Reaching this stage is one of the main goals of data handling.  From here you can use most if not all Python libraries.  And to
# show this we will graph some of our variables using Matplotlib.  We will show you how to use the 'virtual spreadsheet' with
# Matplotlib.

# We will create a graph from the created or calculated variables or 'virtual spreadsheet table' data.
# Create two scatterplots.

fig, ax = plt.subplots()
ax.scatter(Zero_list, W_start_date, color='g')
ax.scatter(E_duration_days, W_end_date, color='b')

# Plot the development over time
for idx in range(len(Zero_list)):
    x1 = Zero_list[idx]
    y1 = W_start_date[idx]
    x2 = E_duration_days[idx]
    y2 = W_end_date[idx]
    ax.plot([x2, x1], [y2, y1], color='r')

# Label the datapoints to make the development more 'visible'
for idx, dates in enumerate(E_labels):
    ax.text(Zero_list[idx], W_start_date[idx], dates, color='g')
    ax.text(E_duration_days[idx], E_end_date[idx], dates, color='b')

# Add titles, labels, and legends to make the graph easy to understand, explain, and clarify graphs.
plt.title('Matplotlib multi-scatterplot/multi-lineplot of Test data')
plt.xlabel('Test Duration in days')
plt.ylabel('Test Weight in lbs')
plt.legend(['Pre test', 'Post test', 'Difference'])

# Let's show the graph
# import os
# os.system('clear')
# plt.show()

# This is a complex graph utilizing complex coding on a small-sized dataset.  When you understand this code, you have reached the
# Master or Research level of computer code engineering at most Universities in Europe.  Congratulations!
# Now we will connect this knowledge to our earlier object-oriented videa lectures.
