# This is lesson 33 from Henrick Johansson's Master Pandas and Python for Data Handling

# Pandas: Pandas File Handling: sql-database files

import pandas as pd
import os
import psycopg2 as ps2
import sqlite3

os.system('clear')
print('\n')

# Carsales = pd.read_csv('python_pandas_for_data_handling/pandas/Carsales.csv', index_col=0)
# Carsales.index.rename('Sales place', inplace=True)

# print(Carsales, '\n')

# Conn creates the database and .to_sql() will be used to creat a 'Carsales_table' table which will be stored in the database.
# Conn = sqlite3.connect('Carsales.db')
# Carsales.to_sql('python_pandas_for_data_handling/pandas/Carsales.db')
# Carsales.to_sql('Carsales_table', Conn, if_exists='replace') # Use append instead of replace if you want to append the Carsales DataFrame
# on every run of this code snippet rather than replace the same Carsales table.

# del Carsales

# Recreate our Carsales DataFrame by loading everything from the Carsales_table.
Conn = sqlite3.connect('python_pandas_for_data_handling/pandas/Carsales.db')
Carsales = pd.read_sql_query('select * from Carsales_table', Conn)

# Restore the indexes to the Pandas DataFrame
Carsales = Carsales.set_index('Sales place')

print(Carsales, '\n')
