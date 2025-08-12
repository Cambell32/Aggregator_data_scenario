#File for combining the fake data generated csv files. 
#
import pandas as pd


#reading file
dfla1= pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_firsthome_rejected_var.csv')
dfla2= pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_nonfirsthome_rejected_var.csv')
dfla3 = pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_investor_rejected_var.csv')
dfla4 = pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_firsthome_drop_var.csv')
dfla5 = pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_investor_drop_var.csv')
dfla6 = pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_nonfirsthome_drop_var.csv')
dfla7 = pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_firsthome_fixed_rejected.csv')
dfla8 = pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_nonfirsthome_fixed_rejected.csv')
dfla9 = pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_investor_fixed_rejected.csv')
dfla10 = pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_firsthome_drop_fixed.csv')
dfla11 = pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_nonfirsthome_drop_fixed.csv')
dfla12 = pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_investor_drop_fixed.csv')
dflacompleted = pd.read_csv('C:/Users/cambe/Desktop/Data Analytics/Data Analyst Scenarios/Connective SaaS scenario/aggre_db_python/loan_application_table_completed.csv')


#concatenating files. 
dfloanapplications = pd.concat([dflacompleted,dfla1,dfla2, dfla3,dfla4,dfla5,dfla6,dfla7,dfla8,dfla9,dfla10,dfla11,dfla12,]).reset_index(drop=True)

#Save to csv after combining
csv_filename = "loan_application_table_allstatus.csv"
dfloanapplications.to_csv(csv_filename, index=False)

print(f"CSV saved as: {'loan_application_table_allstatus'}")