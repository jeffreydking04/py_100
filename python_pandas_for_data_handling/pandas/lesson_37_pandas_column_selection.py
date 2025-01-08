# This is lesson 37 from Henrick Johansson's Master Pandas and Python for Data Handling

# Pandas Operations & Techniques: Column Selection

import pandas as pd
import os

os.system('clear')
print('\n')

Carsales = pd.read_csv('python_pandas_for_data_handling/pandas/Carsales.csv', index_col=0)
Carsales.index.rename('Sales place', inplace=True)

# print(Carsales, '\n')

# Selecting a name, single column as a Pandas series object
# print(Carsales['Tata'], '\n')

# Select a single column and have it returned as a Pandas dataframe
# print(Carsales[['Ford']], '\n')

# print(Carsales[['Ford', 'Mercedes', 'Tata']], '\n') # a df

#              Ford  Mercedes  Tata
# Sales place                      
# One             3         2     9
# Two             0         4     3
# Three           0         0     4
# Four            1         4     1
# Five            6         0     0
# Six            12         3     0
# Seven           5         3     1 

# Change the order of the columns:
# print(Carsales[['Tata', 'Ford', 'Mercedes']], '\n') # a df

#              Tata  Ford  Mercedes
# Sales place                      
# One             9     3         2
# Two             3     0         4
# Three           4     0         0
# Four            1     1         4
# Five            0     6         0
# Six             0    12         3
# Seven           1     5         3 

# Make selections using the .iloc function
# Select column number 1
# print(Carsales.iloc[:, [1]], '\n')


#              Mercedes
# Sales place          
# One                 2
# Two                 4
# Three               0
# Four                4
# Five                0
# Six                 3
# Seven               3 

# Select column number 1 and 2
# print(Carsales.iloc[:, [1, 2]], '\n')

#              Mercedes  Ford
# Sales place                
# One                 2     3
# Two                 4     0
# Three               0     0
# Four                4     1
# Five                0     6
# Six                 3    12
# Seven               3     5 

# Select column number 0 and 1
# print(Carsales.iloc[:, 0:2], '\n') # Notice the difference in syntax here. iloc is followed by brackets in both cases, but when selecting by 
# columns, such as I want column 2 and 5, it looks like this: iloc[:, [2, 5]], where the first colon means give me all rows, then a list
# of the columns desired, but when slicing the columns, it is not a list: .iloc[:, 2:5], which returns 2, 3, 4 


#              Tesla  Mercedes
# Sales place                 
# One              2         2
# Two              6         4
# Three            2         0
# Four             3         4
# Five             0         0
# Six              4         3
# Seven            7         3 

# Column selections can be made using the locate or .loc function
# Select the Ford column
# print(Carsales.loc[:, ['Ford']], '\n')


#              Ford
# Sales place      
# One             3
# Two             0
# Three           0
# Four            1
# Five            6
# Six            12
# Seven           5 

# Select for example the Mercedes and the Tata column
# print(Carsales.loc[:, ['Mercedes', 'Tata']], '\n')

#              Mercedes  Tata
# Sales place                
# One                 2     9
# Two                 4     3
# Three               0     4
# Four                4     1
# Five                0     0
# Six                 3     0
# Seven               3     1 


# print(Carsales.loc[:, 'Mercedes':'Tata'], '\n') # Really neat story: you can slice off of column names.
# But bizarrely the slice in inclusive on both ends!!!!!

#              Mercedes  Ford  Tata
# Sales place                      
# One                 2     3     9
# Two                 4     0     3
# Three               0     0     4
# Four                4     1     1
# Five                0     6     0
# Six                 3    12     0
# Seven               3     5     1 

# Original:
# print(Carsales, '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# One              2         2     3     9       12      1
# Two              6         4     0     3        1      4
# Three            2         0     0     4        0      0
# Four             3         4     1     1        0      0
# Five             0         0     6     0        3      0
# Six              4         3    12     0        1     11
# Seven            7         3     5     1        1     12 

# Select the first column of the df
# print(Carsales.iloc[:, 0], '\n') # returns a series

# Sales place
# One      2
# Two      6
# Three    2
# Four     3
# Five     0
# Six      4
# Seven    7
# Name: Tesla, dtype: int64 

# Select column 2
# print(Carsales.iloc[:, 1]) # returns a series

# Sales place
# One      2
# Two      4
# Three    0
# Four     4
# Five     0
# Six      3
# Seven    3
# Name: Mercedes, dtype: int64

# Select the last column of a df
# print(Carsales.iloc[:, -1]) # returns a series

# Sales place
# One       1
# Two       4
# Three     0
# Four      0
# Five      0
# Six      11
# Seven    12
# Name: Volvo, dtype: int64

# print(Carsales.iloc[:, -1:]) # returns a df

#              Volvo
# Sales place       
# One              1
# Two              4
# Three            0
# Four             0
# Five             0
# Six             11
# Seven           12

# print(Carsales.iloc[:, [-1]]) # returns a df

#              Volvo
# Sales place       
# One              1
# Two              4
# Three            0
# Four             0
# Five             0
# Six             11
# Seven           12

# Instructor opinion: use the df unless you are using other libraries that expect an array or list; series act like arrays

# Selection of both rows and columns using the iloc function
print(Carsales.iloc[0:2, 0:2])

#              Tesla  Mercedes
# Sales place                 
# One              2         2
# Two              6         4
