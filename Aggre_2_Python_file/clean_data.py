#this file is for cleaning and formatting data extracted from the aggre_db 
#it is focused on displaying all good data cleaning and formatting and practices
#
#the end goal is to ensure that data exported as csv into power bi is reliable and without
#corruption. If data is corrupt or missing, averages or inferences, are to be used in 
#those rows where it is present. 
#Reference guide https://datascientyst.com/pandas-cheat-sheet-data-cleaning/

import pandas as pd
from pandas.api.types import * 
from pandas.api.types import is_datetime64_any_dtype as is_datetime

#importing the SQL select function from the aggre_db_select
from aggre_db_select import *

#From aggre_db_select python SQL file, function for running and return a Select query on the aggre.db
df = select('clients')

def Check_Clean(df):
    #Check data if missing
    #Empty check run
    if df.empty:
        print("Error: value empty")
        

#Checking the data. 
 #  df.nuinque()

#Check Duplicates
    df[df.duplicated(keep = False)].index 

#Dropping rows with missing data
    df.dropna(axis=0)    

#Checking and returning column names for checking if data is mixed and formatting below 
    column_names  = df.columns
    for column in column_names: 
        print(column, ':',pd.api.types.infer_dtype(df[column]))

#Applying date formatting to any applicable columns

    for column in column_names:
        
        if is_datetime(df[column]): 
            df[column] = df[column].dt.strftime('%d-%m-%Y')
    return df


df = Check_Clean(df)

#file path and export as CSV file here
export_csv = 'aggre_db_clients.csv' #
path = 'C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_bi_cvs_files/Aggre_2_CSV_files' 
output_file = os.path.join(path,export_csv)
df.to_csv(output_file, index = False)

#os.path.join('aggre_db_SQL_scripts') 
print(f"CSV saved as:{'aggre_db_clients'}")