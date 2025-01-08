# This is lesson 31 from Henrick Johansson's Master Pandas and Python for Data Handling

# Pandas: Pandas File Handling: The .csv file format

# Comma separated data files

# Not defined by a formal standard

import pandas as pd
import os

os.system('clear')
print('\n')

# Read a .csv file named Carsales.csv to a Pandas DataFrame
# Carsales = pd.read_csv('python_pandas_for_data_handling/pandas/Carsales.csv')

# print(Carsales, '\n')

# Here we can see the no-index property of the .csv file.  Our index has been loaded as a data column.
# Let's delete the Carsales DataFrame and make a different attempt to load the DataFrame.
# del Carsales

# Read the .csv file to a Pandas DataFrame and instruct the .read_csv() function to interpret the first column as a an Index Column.
# Let's also rename the Index or Index column after loading the DataFrame.
# Carsales = pd.read_csv('python_pandas_for_data_handling/pandas/Carsales.csv', index_col=0)
# Carsales.index.rename('Sales place', inplace=True)
# print(Carsales, '\n')

# del Carsales

# Pandas .read_csv() function has a huge number of parameters.  The most immediately useful parameter is to use a filepath as filename.
# For example, to replace 'Carsales.csv'...\Documents\Carsales.csv or the suitable
# path to the files location.  Another useful parameter is the sep= which can be used to use other delimiters that the ',' comma.  Using the 
# sep='string delimiter' instead of the default ',' comma.


