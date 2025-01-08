# This is lesson 29 from Henrick Johansson's Master Pandas and Python for Data Handling

# Pandas: Creating Pandas DataFrame objects from scratch

# Begin by importing the Pandas library to use Pandas objecs and functionality
import pandas as pd
import os

def clear_screen():
    os.system('clear')
    print('\n')

clear_screen() # Because I hate typing os.system('clear') for some reason

# Create a Car Data Dictionary with ficticious car sales data
Cardata = {
    'Mercedes': [2, 4 ,0, 4, 0, 3],
    'Ford': [3, 0, 0, 1, 6, 12],
    'Tata': [9, 3, 4, 1, 0, 0],
    'Renault': [12, 1, 0, 0, 3, 1],
}

# Use Pandas constructor function Dataframe() to create a Pandas DataFrame
Carsales = pd.DataFrame(Cardata)

# Print the DataFrame to screen to check that everything was created as intended.
# print(Carsales, '\n')

# Edit the Index and Index Labels of the existing DataFrame
Carsales.index.rename('Sales place', inplace=True)

# print(Carsales, '\n')

# Rename the index labels using a Python Dictionary.
Carsales.rename(index={
    0: 'One',
    1: 'Two',
    2: 'Three',
    3: 'Four',
    4: 'Five',
    5: 'Six',
}, inplace=True)

# print(Carsales, '\n')

# Word of advice: Setting the index labels is normally best done lately, in the report stage of any data analysis.
# Data sorting may, for example, interfere with the visual aspect of the naming convention related the order of the data in
# this DataFrame used in this example.  Renaming of key variables that are necessary to identify a data observation is not advised.
# Use a new column or make the naming changes as a graphical last stage edit instead.

# The Index and Index Labels are very useful for data selections, try this query as an example.
# print(Carsales.loc['Two'], '\n')

# Add a new row with index labels to the DataFrame using a Python Dictionary, the Pandas constructor, and the Pandas concat function
new_sales_place = pd.DataFrame({
    'Mercedes': 3,
    'Ford': 5,
    'Tata': 1,
    'Renault': 1,
}, index=['Seven'])
Carsales = pd.concat([Carsales, new_sales_place])

# print(Carsales, '\n')

# Add new columns to the DataFrame using Python lists.
Volvo = [1, 4, 0, 0, 0, 11, 12]
Tesla = [2, 6, 2, 3, 0, 4, 7]
Carsales['Volvo'] = Volvo

# print(Carsales, '\n')

# Insert and name a column at a defined position in the DataFrame with the insert instruction.
Carsales.insert(loc=0, column='Tesla', value=Tesla)

# print(Carsales, '\n')

# Create a DataFrame for Python Lists
# Reuse Volvo and Tesla. Add Ford.
Ford = [3, 0, 0, 1, 6, 12, 5]

data = [
    Volvo,
    Tesla,
    Ford,
]

# print(data, '\n') # [[1, 4, 0, 0, 0, 11, 12], [2, 6, 2, 3, 0, 4, 7], [3, 0, 0, 1, 6, 12, 5]] 

# Create the Pandas DataFrame
Carsales_2 = pd.DataFrame(list(zip(Volvo, Tesla, Ford)), columns=['Volvo', 'Tesla', 'Ford'])
# The .zip() function creates a Python tuple for every position in the list (Volvo[0], Tesla[0], Ford[0]), (Volvo[1], Tesla[1], Ford[1])...
# print(Carsales_2, '\n')

# We can conclude that currently the Dictionary with list data presents the least work avenue to create DataFrames without
# using transpose functions.

# Time to prepare for the next lecture and time to learn to save our Carsales DataFrame to the .csv (comma-separated) file format and 
# to the .xlsx file format.

Carsales.to_csv('python_pandas_for_data_handling/pandas/Carsales.csv')
Carsales.to_excel('python_pandas_for_data_handling/pandas/Carsales.xlsx')

# This is how you delete a DataFrame
del Carsales
print(Carsales) # NameError
