# This is lesson 38 from Henrick Johansson's Master Pandas and Python for Data Handling

# Pandas Operations & Techniques: Row Selection

import pandas as pd
import os

os.system('clear')
print('\n')

Carsales = pd.read_csv('python_pandas_for_data_handling/pandas/Carsales.csv', index_col=0)
Carsales.index.rename('Sales place', inplace=True)

# print(Carsales, '\n')

# Note: Remember .iloc and .loc syntax model df.loc[row, column]
# jk: When selecting columns, we need loc or iloc[:, colunmn_selection_syntax], but when selecting rows,
# jk: we can drop the column part loc[row_selection_syntax]
# jk: Perhaps best practice is to be explicit when selecting only rows: .iloc[row_selection_syntax, :]

# Select a single row with the .loc function
# print(Carsales.loc['Three', :], '\n') # a series
# print(Carsales.loc['Three'], '\n') # equivalent

# Tesla       2
# Mercedes    0
# Ford        0
# Tata        4
# Renault     0
# Volvo       0
# Name: Three, dtype: int64 

# The .iloc function and its type of integer selection is different
# print(Carsales.iloc[3, :], '\n') # Does not select row 'Three' or row number 3 but 4.

# Tesla       3
# Mercedes    4
# Ford        1
# Tata        1
# Renault     0
# Volvo       0
# Name: Four, dtype: int64 

# This code selects row number 3 with the .iloc function:
# print(Carsales.iloc[2, :], '\n')

# Tesla       2
# Mercedes    0
# Ford        0
# Tata        4
# Renault     0
# Volvo       0
# Name: Three, dtype: int64 

# This code doesn't select all rows between 2 and 4 but all rows between labels 'Two' and 'Four'
# print(Carsales['Two':'Four'], '\n') # a df

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# Two              6         4     0     3        1      4
# Three            2         0     0     4        0      0
# Four             3         4     1     1        0      0 

# jk: The above is not loc or iloc.  It is direct. Does this work?
# print(Carsales['Two':'Four', :], '\n') # a df

# jk: It does not.

# Note: 'In this case' the df labels are ordered after the labels corresponding number.  In another case,
# the df could be sorted differently yielding a different outcome of this aggregation.
# jk: ???

# This function selects all rows between row number 3 and 4.
# print(Carsales.iloc[2:4, :], '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# Three            2         0     0     4        0      0
# Four             3         4     1     1        0      0 

# Selects row number 2, 3, and 4
# print(Carsales.iloc[1:4, :], '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# Two              6         4     0     3        1      4
# Three            2         0     0     4        0      0
# Four             3         4     1     1        0      0 

# Some special row solections using the .iloc and .loc functions
# print row 0 to 4
# print(Carsales.iloc[:4, :], '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# One              2         2     3     9       12      1
# Two              6         4     0     3        1      4
# Three            2         0     0     4        0      0
# Four             3         4     1     1        0      0

# Print 5 to the last row number
# print(Carsales.iloc[4:, :], '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# Five             0         0     6     0        3      0
# Six              4         3    12     0        1     11
# Seven            7         3     5     1        1     12 

# Print 'Three' to the last
# print(Carsales.loc['Three':, :], '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# Three            2         0     0     4        0      0
# Four             3         4     1     1        0      0
# Five             0         0     6     0        3      0
# Six              4         3    12     0        1     11
# Seven            7         3     5     1        1     12 

# Print 'Three' to the first, including the first
# print(Carsales.loc[:'Three', :], '\n')


#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# One              2         2     3     9       12      1
# Two              6         4     0     3        1      4
# Three            2         0     0     4        0      0 

# We can print every other row
# print(Carsales.iloc[::2, :], '\n') # step: start_index_inclusive:end_index_exclusive:step works on lists too, not just dfs

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# One              2         2     3     9       12      1
# Three            2         0     0     4        0      0
# Five             0         0     6     0        3      0
# Seven            7         3     5     1        1     12 

# Print the rows backwards
# print(Carsales.iloc[::-1, :], '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# Seven            7         3     5     1        1     12
# Six              4         3    12     0        1     11
# Five             0         0     6     0        3      0
# Four             3         4     1     1        0      0
# Three            2         0     0     4        0      0
# Two              6         4     0     3        1      4
# One              2         2     3     9       12      1 

# jk: So completely reflect the df along both axes:
# print(Carsales.iloc[::-1, ::-1], '\n')

#              Volvo  Renault  Tata  Ford  Mercedes  Tesla
# Sales place                                             
# Seven           12        1     1     5         3      7
# Six             11        1     0    12         3      4
# Five             0        3     0     6         0      0
# Four             0        0     1     1         4      3
# Three            0        0     4     0         0      2
# Two              4        1     3     0         4      6
# One              1       12     9     3         2      2 
