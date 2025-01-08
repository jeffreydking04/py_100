# This is lesson 32 from Henrick Johansson's Master Pandas and Python for Data Handling

# Pandas: Pandas File Handling: The .xlsx file format

import pandas as pd
import os

os.system('clear')
print('\n')

# Read the Carsales.xlsx file to a Pandas DataFrame
# Carsales = pd.read_excel('python_pandas_for_data_handling/pandas/Carsales.xlsx')

# print(Carsales, '\n')

# Read a Carsales.xlsx file to a Pandas DataFrame, restore the index labels and name the index column.
Carsales = pd.read_excel('python_pandas_for_data_handling/pandas/Carsales.xlsx', index_col=0)
Carsales.index.rename('Sales place', inplace=True)

# print(Carsales, '\n')

# Write every column into its own Excel spreadsheet.  Please note that this is just a simple way of creating a workbook
# with many spreadsheets.
# with pd.ExcelWriter('Carsales2.xlsx') as Xlxs_writer:
#     for column in Carsales.columns:
#         Carsales[column].to_excel(Xlxs_writer, sheet_name=column)

# Read the spreadsheets back to DataFrame format.
Carsales2 = pd.read_excel('python_pandas_for_data_handling/pandas/Carsales2.xlsx', index_col=0, sheet_name=[
    'Mercedes',
    'Ford',
    'Tata',
    'Renault',
])

# print(Carsales2)

# The resulting solution is not satisfactory. Let's try again.
# This code reconstructs the spreadsheets into a satisfactory Carsales3 DataFrame with the aid of  Pandas concat() function used
# on a column basis (axis=1) instead of a row basis (axis=0, or default mode)
Carsales3 = pd.DataFrame()
for dct in Carsales2.values():
    Carsales3 = pd.concat([
        Carsales3,
        # pd.DataFrame.from_dict(dct)   jk: This is the code he used, but these 'dct's are already dataframes so the following works (his code works too)
        dct
    ], axis=1)

print(Carsales3, '\n')


