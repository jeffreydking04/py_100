# This is lesson 35 from Henrick Johansson's Master Pandas and Python for Data Handling

# Pandas Operations & Techniques: Object Inspection

import pandas as pd
import os

os.system('clear')
print('\n')

Carsales = pd.read_csv('python_pandas_for_data_handling/pandas/Carsales.csv', index_col=0)
Carsales.index.rename('Sales place', inplace=True)

# print(Carsales.info(), '\n')

# Take a look at a returned Series object from a DataFrame
# print(Carsales['Tata'].info(), '\n')

# <class 'pandas.core.series.Series'>
# Index: 7 entries, One to Seven
# Series name: Tata
# Non-Null Count  Dtype
# --------------  -----
# 7 non-null      int64
# dtypes: int64(1)
# memory usage: 112.0+ bytes
# None 


# Take a look at a returned dataframe object of the same dimensions
# print(Carsales['Tesla'].info())

# <class 'pandas.core.series.Series'>
# Index: 7 entries, One to Seven
# Series name: Tesla
# Non-Null Count  Dtype
# --------------  -----
# 7 non-null      int64
# dtypes: int64(1)
# memory usage: 112.0+ bytes
# None

# Print the object type inside a Pandas DataFrame cell
# print(type(Carsales.loc['Two', 'Ford'])) # <class 'numpy.int64'> numpy, not python

# Let's test this more thoroughly 
# print(type(Carsales.iloc[2, 2])) # <class 'numpy.int64'>

# Let's create a Python int for comparison
x = 4
# print(type(x)) # <class 'int'>

# Let's make a test with the Dtypes function
# print(Carsales.dtypes, '\n')

# Tesla       int64
# Mercedes    int64
# Ford        int64
# Tata        int64
# Renault     int64
# Volvo       int64
# dtype: object 

# Let's make another test with the locate function
y = Carsales.loc['Two', 'Ford']
# print(type(y), '\n') # <class 'numpy.int64'> 

# print(type(int(y)), '\n') # <class 'int'> 

# This code shows how to get the data back to Python variables/objects (if necessary)
# The tolist() method can also be used on non-collection objects.

z = Carsales.loc['Two', 'Ford'].tolist()
# print(type(z), '\n') # <class 'int'> 

# A very smart option is to use the column-based Pandas function .to_list()
lst = Carsales.Ford.to_list()
for n in lst:
    print(type(n)) # <class 'int'>

# Numpy also has a number of methods to convert Numpy objects to Python objects, for example numpy.ndarray.item
