#Python SQL file for inserting data into the aggre_db. 
#it calls function appBrokeridFix from the clean_data file prior to processing any data queries into insert.
#note that it is currently inactive. 

import sys 
import os 
import pandas as pd
from mysql.connector import Error 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Aggre_2_Files_Github')))

#file that contains the dbconnect function 
from aggre_db_SQL_connect_scripts import dbconnect

#from clean_data import appBrokeridFix - fix for broken data values
#dfapp = pd.read_csv('aggre_db_cvs_files/inactive_loanapplication_table.csv')
#
#cleaned = appBrokeridFix(dfapp)
#csv_filename = "cleaned_data.csv"
#cleaned.to_csv(csv_filename, index=False)
#convert into a clean cvs file here for insertion into the table of db aggre

#clean data csv 
app_data = pd.read_csv('Aggre_2_Files_Github/loan_applications_aggre.csv')
file_path = 'Aggre_2_Files_Github/loan_applications_aggre.csv'

conn = dbconnect()
cursor = conn.cursor()
query = f"""LOAD DATA LOCAL INFILE'{file_path}' 
INTO TABLE loan_applications
FIELDS terminated by ','
ENCLOSED by '"' 
LINES TERMINATED BY '\\n' 
IGNORE 1 LINES 
(app_application_id, app_client_id, app_broker_id, app_lender_id, app_status,
 app_lodgement_date, app_amount_requested, app_product_id, app_marketing_id, app_last_updated)
;"""

try:
    cursor.execute(query)
    conn.commit()
    print("Data loaded successfully.")

except Error as e:
        print(f"❌ Error: {e}")
finally:
        cursor.close()
        conn.close()
