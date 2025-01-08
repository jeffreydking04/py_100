# This is lesson 25 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python Object Oriented Programming III: Files and Tables

# Libraries
import pickle
import csv
import pandas as pd
from openpyxl import workbook

class Mailcat_object():
    def __init__(self, id_name, mail_address, list_items=[]): # This function creates an instance of the class
        self.idnum: int # We will use this as an id-number
        self.id_name = id_name # Name of the record in our Mail Catelog
        self.mail_address = mail_address # mail data
        self.list_items = list_items # List of arbitrary data items/objects

    def get_id_name(self): # these methods show how to create methods in objects
        return self.id_name # Returns a string
    
    def get_mail_address(self): # Returns a string
        return self.mail_address
    
    def get_list_items(self): # Returns a list of arbitrary objects/items
        return self.list_items

# Class 'Mailcat_collection' with a dictionary, using id_number as key
class Mailcat_collection():
    def __init__(self):
        self.Mailcat = {} # Dictionary with idnum as key and Mailcat_objects as values
        self.index_counter = 0 # This is the first key number

    def addMailcat_object(self, Mailcat_object):
        self.index_counter += 1 # Creates the nex idnum to be used with the dictionary
        Mailcat_collection.idnum = self.index_counter # key number
        self.Mailcat.update({Mailcat_collection.idnum: Mailcat_object}) # This line updates the dictionary with a key and value

# Create a class which 'encapsulates' our Mailcatalogue and adds four start entries into the Mailcat_collection object 'named data'
# and the class will have two functions for printing and flattening the object's data
class create_catalog():
    def __init__(self):
        self.data = Mailcat_collection()
        self.data.addMailcat_object(Mailcat_object('Joe', 'joe.joe@gmail.com', [1200, 99.3, 0, 0.0, 'value', 'compl%']))
        self.data.addMailcat_object(Mailcat_object('Anand', 'anand.anand@aol.com', [1300, 75.3, 4, 33.3, 'value', 'compl%', 'Time_c', 'answ%']))
        self.data.addMailcat_object(Mailcat_object('Lisa', 'lisa@gmx.com', [2400, 45.5, 0, 0.0, 'value', 'compl%']))
        self.data.addMailcat_object(Mailcat_object('Mohammed', 'mohammed@gmail.com', [1700, 82.3, 0, 0.0, 'value', 'compl%']))

    def list_Mailcat_objects(self):
        dct = self.data.Mailcat
        for key, value in dct.items():
            mail = value  # Get the object instance and print the relevant data values and objects
            print(mail.id_name, mail.mail_address, mail.list_items)

    def serialize_Mailcat_objects(self):
        dct = self.data.Mailcat
        ret_list = []
        header = ['Name', 'mail_address', 'integer1', 'float1', 'integer2', 'float2', 'string1', 'string2', 'string3', 'string4']
        ret_list.append(header)
        for key, value in dct.items():
            mail = value # delivers the object instance to our function and print relevant data values and objects
            list_string = ' '.join([str(item) for item in mail.list_items])
            mail_string = str(mail.id_name) + ' ' + str(mail.mail_address) + ' ' + list_string
            ret_list.append(mail_string.split(' '))
        return ret_list

# We begin by loading our Mail catalog from our pickle file
file = open('pandas/Mail_c.obj', 'rb')
Mail_c = pickle.load(file)
file.close()
Mail_c.list_Mailcat_objects()

# Let's begin by 'flattening' our objects into strings on the tabular form and create a .csv file (comma seperated file)
Mail_c2 = Mail_c.serialize_Mailcat_objects()
print(Mail_c2)
for item in Mail_c2:
    print(item)

# Opening a csv file in write mode
with open('pandas/mail_cat.csv', 'w', newline='') as csvfile:
    # use csv.writer to write the list ot the csv file
    writer = csv.writer(csvfile)
    writer.writerows(Mail_c2) # use writerow for a list of single strings and writerows for a list of lists
# The file closes after finishing the with code block.
# This .csv flie has a tabular form, and is useful for direct use with most libraries and programs.
# This code shows how to convert this .csv file to an Excel workbook, and how to load the .csv file into a Pandas DataFrame

# Let's begin with Excel, which is the main data storage standard for everyday home or business data, with an estimated 100
# to 500 million unique users.

csv_temp = [] # temporary storage
with open('pandas/mail_cat.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csv_temp.append(row)
    
workbook = workbook.Workbook() # Create a new workbook
sheet = workbook.active # Sets the sheet as active sheet in the workbook
for row in csv_temp:
    sheet.append(row)
workbook.save('pandas/mail_cat.xslx')

# Print the Excel document file using the the openpyxl library
for row in sheet.iter_rows():
    row_list = []
    for cell in row:
        row_list.append(str(cell.value) + ' ')
    print(row_list)

# We can load our .csv file into a Pandas DataFrame for use with Pandas.  Pandas is a Python library with a very large user base
# estimated at 5-10 million users. Pandas is considered to be an Excel spreadsheet with extende+++++ capabilities for data science
# and all types of machine learning.
Mailcat_DataFrame = pd.read_csv('pandas/mail_cat.csv', delimiter=',')
print(Mailcat_DataFrame)
