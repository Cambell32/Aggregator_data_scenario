import sys 
import os 
import pandas as pd
from mysql.connector import Error 
#file that contains the dbconnect function 
from aggre_db_SQL_connect_scripts import dbconnect

#tables from the aggre_db to select from: 
#client_table; loan_applications; marketing; product; user
def select(table):
    conn = dbconnect()
    cursor = conn.cursor()

    query = "SELECT * FROM "  + table
    cursor.execute(query)

    result = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    
    df = pd.DataFrame(result, columns= column_names )
    return df

#for each loan_application row, the column value has to be taken from the second array of the loan_application list, those are the 
# columns of the the loan_application SQL result