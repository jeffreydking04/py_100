# Import libraries/modules datetime and matplotlib.pyplot
import datetime as dt
import matplotlib.pyplot as plt

# Read a Text_file.txt into a read_datas list of strings. The file can be downloaded from the course page or 
# be created with downloadable .py file. This read .txt file code can be adapted to almost any type of data
# text file and the .py file contains advanced data handling code.
read_datas = []
read_counter = 0
with open('Text_file.txt') as input_file:
    # read_datas = input_file.readlines() This Alternative is a 1-chunk does it all code for small files
	for read_data in input_file:
		read_datas.append(read_data)
		read_counter += 1
input_file.close()
print(read_counter) # print the number of read lines code/file test. This shows the number or readlines
print(read_datas[0])  # print the header
print(read_datas)

# Use a function to split our list of strings into lists. Split on whitespace
def split_data(list=[]):
	hder = []
	Bd = []
	Esd = []
	Eed = []
	Wsd = []
	Wed = []
	newline = []
	for data in read_datas:
		if read_datas.index(data) == 0:  # This is a special treatment of the header.
			hder = data.split(" ")
			del hder[-1] # Delete newline
		else:
			words = data.split(" ")	
			Bd.append(words[0])
			Esd.append(words[1])
			Eed.append(words[2])
			Wsd.append(words[3])
			Wed.append(words[4])
			newline.append(words[5])
	del newline   # the newlines are a feature of the .txt file, used to structure data
	return hder, Bd, Esd, Eed, Wsd, Wed

# USe the split_data function to create a list of headers and 5 lists of variables	
Header, Birth_date, E_start_date, E_end_date, W_start_date, W_end_date = split_data(read_datas)

# Print variables to make a check that the code created the desired results 
print(Birth_date)
print(W_end_date)
print(Header)

# Convert the data to useable formats. Header is string, Birth_data should be converted to DateTime.
# E_start_date and E_end_date are strings compatible with DateTime. W_start_date and W_end_date are Strings 
# directly convertible to integers.
# Creating DateTime objects and converting strings to ints. *This code assumes that all lists are of equal length*
for date in range(len(Birth_date)):
	Birth_date[date] = dt.datetime.strptime(Birth_date[date], '%Y/%m/%d')
	E_start_date[date] = dt.datetime.strptime(E_start_date[date], '%Y-%m-%d')
	E_end_date[date] = dt.datetime.strptime(E_end_date[date], '%Y-%m-%d')
	W_start_date[date] = int(W_start_date[date])
	W_end_date[date] = int(W_end_date[date])

print(Birth_date[0])   # This is an interesting feature of DateTime objects and Lists... Warning.
print(E_end_date)
print(W_end_date)

# Calculate more variables with more practical use
E_Duration_days = []   # This is the duration of a test in days
Age_at_E_years = []    # This is the test subjects age when the test ends
Zero_list = []         # This is a list of zeroes useful with the duration varibale
E_labels = []          # This is a label variable useful for graphs.
for date in range(len(Birth_date)):
	E_Duration_days.append((E_end_date[date] - E_start_date[date]).days)
	Age_at_E_days = E_end_date[date] - Birth_date[date]
	Age_at_E_years.append(Age_at_E_days.days//365)
	E_labels.append("E" + str (date + 1))
	Zero_list.append(0)

print(E_Duration_days)
print(Age_at_E_years)
print(E_labels)

# This code has created a List header variable containing the names the base variables. There is a dataset 
# of five lists with base variables named Birth_date, E_start_date, E_end_date, W_start_date, W_end_date
# and there are four lists of calculated variables. In total there is 10 lists and 9 of these lists can
# be said to form av virtual "spreadsheet" or columns only linked to each other through the order of 
# the data elements in the lists.
# Reaching this stage is one of the main goals of data handling. From here it is possible to use most Python 
# libraries and graph these variables, and we will show you how to use this "spreadsheet table" with Matplotlib

# Create a two scatterplot graph from the manufactured "spreadsheet table" data
fig, ax = plt.subplots()
ax.scatter(Zero_list, W_start_date, color='g')
ax.scatter(E_Duration_days, W_end_date, color='b')

# Plot development over time
for m in range(len(Zero_list)):
	x1 = Zero_list[m]
	y1 = W_start_date[m]
	x2 = E_Duration_days[m]
	y2 = W_end_date[m]
	ax.plot([x2, x1], [y2, y1], color = 'r')

# Label the data points to make the development more visible
for n, dates in enumerate(E_labels):
    ax.text(Zero_list[n], W_start_date[n], dates, color='g')
    ax.text(E_Duration_days[n], W_end_date[n], dates, color='b')

# Titles, labels, and legends explain and clarify graphs with labels
plt.title('Matplolib scatterplot of Test data')
plt.xlabel('Test Duration in days')
plt.ylabel('Test weight in lbs')
ax.legend(['Before test', 'After test', 'Difference'])

# Show the graph on your screen
plt.show()


# This solution creates a complex graph utilizing complex code on a small-sized dataset. When you understand this code 
# you have reached the Master or researcher level of computer code engineering at most Universities in Europe. 
# Congratulations!

# Let's connect this knowledge to our earlier object-oriented video lectures. Remember the Mailcat object class from the 
# video lectures about Dictionaries and object oriented programming?

# One way to connect the code from this video lecture to the earlier OOP video lectures is to enter our data into the list_items 
# Python List=[] class inside the custom Mailcat_objects, preferably as a dictionary with the data entered into a list as 
# the Dictionary's data values.
class Mailcat_object():
    def __init__(self, id_name, mail_adress, list_items=[]):  # Creates an instance of this class
        self.idnum: int  # idnumber 
        self.id_name = id_name  # name 
        self.mail_adress = mail_adress # mail data 
        self.list_items = list_items 	# arbitrary data items in list. For example Dictionaries showing a test/experiment
										# for the particular Mailcat Object. Every added new Dictionary could be a new test/experiment 

    def get_id_name(self):  # These methods only shows how to create methods.
        return self.id_name  # Returns string
    def get_mail_adress(self): 
        return self.mail_adress  # Returns string
    def get_list_items(self):
        return self.list_items # Returns a list of arbitrary objects
