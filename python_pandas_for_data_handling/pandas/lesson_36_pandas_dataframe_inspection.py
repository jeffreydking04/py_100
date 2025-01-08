# This is lesson 36 from Henrick Johansson's Master Pandas and Python for Data Handling

# Pandas Operations & Techniques: DataFrame Inspection

import pandas as pd
import os

os.system('clear')
print('\n')

Carsales = pd.read_csv('python_pandas_for_data_handling/pandas/Carsales.csv')
Carsales.index.rename('Sales place', inplace=True)
Carsales_N = pd.concat([Carsales]*5000, ignore_index=True)

# print(Carsales_N)

# Try the .head() function (5 is the default)
# print(Carsales_N.head())

# 20 rows can be a useful inspection number.
# print(Carsales_N.head(20))

# The .tail() function shows the bottom of the DataFrame
# print(Carsales_N.tail(20), '\n')

# What if we want to inspect a selection from the middle, somewhere in the DataFrame?
# print(Carsales_N.iloc[5000:5021, :])

# Print the entire Carsales_N DataFrame as a String.  Note: This is not a recommended option for large DataFrames.  Reason
# can be checked by adding a zero or two to the '5000 and when you run the code, you will either get a warning messages or a crash.
# print(Carsales_N.to_string())

# You can use various functions to iterate through the dataframe and print every row (no good solutions without... either relaxing
# safety parameters or using imported vectorization techniques or libraries from other coding libraries or languages).
# Let's try a Python iterator (slow, cumbersome, turns every row into a tuple and print the tuple, tuple, for tuple).
# for row in Carsales_N.itertuples():
#     print(row)

# Import more developed visualization libraries...
# from IPython.display import display

# pd.set_option('display.max_rows', None)
# display(Carsales_N)
# pd.reset_option('display.max_rows') # pd.reset_option('all')

# The above didn't do anything in vs_code terminal, but was really nice on jupyter

# The computers, depending on the hardware, software, settings, and other parameters may crash even when trying to print or look at
# even modest DataFrames or similar data-items.  This is why we need the .head() and .tail() functions plus, of course, some assistance
# from functions such as .iloc(), the .loc(), and support libraries in order to properly inspect the contents of DataFrames.
