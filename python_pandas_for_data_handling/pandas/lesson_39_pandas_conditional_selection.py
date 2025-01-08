# This is lesson 39 from Henrick Johansson's Master Pandas and Python for Data Handling

# Pandas Operations & Techniques: Conditional Selection

import pandas as pd
import os

os.system('clear')
print('\n')

Carsales = pd.read_csv('python_pandas_for_data_handling/pandas/Carsales.csv', index_col=0)
Carsales.index.rename('Sales place', inplace=True)

# print(Carsales, '\n')

# Use .loc function to select all salesplaces where at least one Mercedes has been sold
Mercedes_sales = Carsales.loc[Carsales.Mercedes > 0]
# print(Mercedes_sales, '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# One              2         2     3     9       12      1
# Two              6         4     0     3        1      4
# Four             3         4     1     1        0      0
# Six              4         3    12     0        1     11
# Seven            7         3     5     1        1     12 

# Extend the earlier example to the two logical statements and this time we select all sales place with at least one Mercedes sold
# and one Ford sold.
Mercedes_Ford_sales = Carsales.loc[(Carsales.Mercedes > 0) & (Carsales.Ford > 0)] # parentheses needed
# print(Mercedes_Ford_sales, '\n')


#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# One              2         2     3     9       12      1
# Four             3         4     1     1        0      0
# Six              4         3    12     0        1     11
# Seven            7         3     5     1        1     12 

# Use of the .iloc function for the same selections
Mercedes_sales_2 = Carsales.iloc[list(Carsales.Mercedes > 0)]
# print(Mercedes_sales_2, '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# One              2         2     3     9       12      1
# Two              6         4     0     3        1      4
# Four             3         4     1     1        0      0
# Six              4         3    12     0        1     11
# Seven            7         3     5     1        1     12 

# Let's extend the use of the .iloc function to two logical requirements
Mercedes_Ford_sales_2 = Carsales.iloc[list((Carsales.Mercedes > 0) & (Carsales.Ford > 0))]
# print(Mercedes_Ford_sales_2, '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# One              2         2     3     9       12      1
# Four             3         4     1     1        0      0
# Six              4         3    12     0        1     11
# Seven            7         3     5     1        1     12 

# jk: .iloc not intuitive in this case; is there a use case where .iloc conditionals are preferable?

# More examples of possible conditional selections using the .loc() function.
sales_place_list = ['Two', 'Six']
# Use the .loc function to select rows conditional on the constant of a list
# selected_sales = Carsales.loc[sales_place_list] # this works, but he did it like:
selected_sales = Carsales.loc[Carsales.index.isin(sales_place_list)]
# print(selected_sales, '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# Two              6         4     0     3        1      4
# Six              4         3    12     0        1     11 

# The .loc function can be used to select conditional on strings
selected_index_labels = Carsales.loc[Carsales.index.str.contains('Five')]
# print(selected_index_labels, '\n')


#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# Five             0         0     6     0        3      0 

# The .loc function can be extended to make selections between values
sales_places_between = Carsales.loc[Carsales['Ford'].between(2, 20)]
# sales_places_between = Carsales.loc[Carsales.Ford.between(2, 20)] # also works; basically highlighting the fact that DF allows dot notation
print(sales_places_between, '\n')

#              Tesla  Mercedes  Ford  Tata  Renault  Volvo
# Sales place                                             
# One              2         2     3     9       12      1
# Five             0         0     6     0        3      0
# Six              4         3    12     0        1     11
# Seven            7         3     5     1        1     12 
