Updates: 
20/05/2025
Added product_lender_id to table Products in order to track lender to broker activity and query highest, lowest, most and least quantities to support product development by the aggregator business.

DDL design decision: 
Dropped the app_lender_id column from loan_applications table as it was redundant because related data could be traced and retrieved via product  table to the lender table. 

Updates: 
25/05/2025

Created file directories aggre_db_SQL and aggre_db_python for handling relevant files. 

Currently, write insert query into db next. 

30/05/2025
Unfortunately, the data login/host details were corrupted, so the installation was removed and reinstalled. 

The entire db schema requires being rebuilt from scratch. 

31/05/2025
The entire db schema was rebuilt from the csv file structures of each table. 

The data was inserted via a python-sql script. 

The data was then checked, ordered and manually changed using case statements in order to ensure that the primary-foreign key relations can be maintained between tables. 

Completed. 

Data Scenario considerations.
REMOVED ADMIN from user TABLE
Without the event / process log table, and the scenario focusing on just the operational / commercial data side of the aggre db, 
user = admin query run and removed those values from the user table. 
Removed due to redundancy in light of data scenario. 


DROPPED PRODUCT ORGANIZATION ID From product table - lender id 
Redundant column as the relation between product and broker is reflected in the loan application table
as referenced in the app_broker_id column of the loan application table. 

DROPPED USER_CREATED_AT column from user table 
Dropped the column as those values were beyond the scope of the data scenario (the customer & broker & lender data). 
Similar logic to removing ADMIN from user table as the scope of scenario was looking at product and commercial value of the 
data rather than HR or accessibility issues etc.  

BEST OF ALL DATE VALUES READDED TO LOAN_APPLICATION TABLE 
there was an error loading these values initially and so the table 
was truncated. This has since been fixed with new values being generated and 
added. These date values were essential for projection and historical 
data analytical purposes. 

10/06/2025 & 12/06/2025 
Currently moving into more sophisticated business scenario data. Generating data for calculating expenses to establish ROI and COAC figures. 

As well as this, to figure out forecasting in future for those expenses as well. 

Moreover, as the aggregator scenario is about the delivery and networking of SAAS to lenders and brokers, then revenue is calculated through the loan application amounts as well. 

This data can be calculated based off price setting for the average / median amounts of the loan applications as an aggregate. 

13/06/2025 & 15/06/2025 
Running a select all query on the MariaDB for marketing and loan application amounts. 

Have successfully created the query to do so. 

Now am leaning back into python and pandas where I'll be answering the business question: "what was the average ROI on marketing expenses per each successful loan application". 

I want to answer this business question in two ways. 

The first step is simply retrieving all the data from the database and manipulating it in Visual Studio Code. 

The second: writing up a second SQL query, using joins, then returning all marketing data and the loan applications they match to where the status condition is 'success' 

16/06/2025
Currently working on a solution for calculating business questions like ROI and CAC. 

In SQL I am trying to export app_amount totals per broker in order to determine the organization then they're linked to in order to apply a percentage as a broker fee. 

In Python, I am trying to find a way to export a CSV file into Power BI from app_amounts, where marketing expenses are calculated and plotted per app_lodgement date.

22/06/2025

Have successfully run an ETL: running Python SQL scripts to get conditionally transformed data before power querying it and then loading it all into Power BI. This was satisfying.  

These are the five domains that I need to become at least proficient in. PYTHON,  SQL, Excel and Power BI. 

24/06/2025 
Currently working on two sets of SQL-Python-CSV retrieved data in Power BI: reviewing the submitted and completed data. 

I did have an initial issue trying to merge all the dataframe reindexed data in Excel via a Power Query. The workaround involved each one of those tables
being re-indexed, yet again, in Power BI. It should be noted: I would not use this solution IF I wasn't 100% sure about the data that I was
performing this indexation of to merge the data frames. 

That said, the indexing solution did merge, allowing me to run a left join on all matching columns. This is where, if I wasn't familiar with the data I could potentially get away 
with the index solution in Power Query. 

The total number of rows was identical across all of the dataframes. 

I am currently working on the data in Power BI. 

The NEXT GOAL: 
Table Join & CTE inside of SQL before trying to map these out in Python. 

Although my hunch is that, I have completed the vast majority of the technical/coding side of Data Analytics. 

Now it is high time that I complete the analysis of this dataset. 

26/06/2025
I want to achieve the below and these are the comments from SQL that I am attempting to turn into queries. 
-- SELECT DISTINCT app_broker_id as BI from loan_application; 
-- SELECT user_organization_id as Org_ref from user WHERE user_id = BI;
-- CTE to retrieve loan amounts per organization id 
-- Select organization_name as Organization from organization where organization_id = Org_ref 

Completed a right join table query, where organization_id are returned based on a match 
on the user table between user user_id and loan_application app_broker_id. 

Now, I am planning on using this as the alias part of a CTE query to return names for each organizational_id 
before exporting all the data out of the Maria DB as a CSV file. 

27/06/2025

SELECT article.* , section.title, category.title, user.name, user.name
FROM article
INNER JOIN section ON article.section_id = section.id
INNER JOIN category ON article.category_id = category.id
INNER JOIN user ON article.author_id = user.id
LEFT JOIN user ON article.modified_by = user.id
WHERE article.id = '1'

This is a potential structural solution to my query for retrieving values from loan_application, user, organization tables to apply organization names from organization table
to the returned table combining the user and loan application data for a csv export to Power BI. 



- constructing query:SELECT loan_application.app_application_id, loan_application.app_amount_requested, loan_application.app_status, product.product_id, organization.organization_id, organization.organization_name  
FROM loan_application 
INNER JOIN loan_application ON product.product_id = loan_application.app_product_id 
INNER JOIN product ON organization.organization_id = product.product_lender_id

06/07/2025
Currently, there is a MySQL issue that means the server cannot be generated, I will be deleting the entire installation and reinstalling. Fortunately, I have enough data on hand to 
complete the original data project objectives; however, the data project is currently in its visual analytics phase which is being completed in Power BI. 

08/07/2025
Following a catastrophic error with xamp installation, xamp had to be uninstalled and reinstalled. 
Handily, I think the issue was a MySQL data folder that contained all the parameters, properties etc. for the db. I confirmed 
this when I attempted to swap out a backup for the MySQL folder that was reinstalled and when I attempted to launch phpMyAdmin
that is when the errors occurred. 

Now with the reinstallation complete and phpMyAdmin working as intended, I have recreated all of the tables and made some additions were applicable. 
That said, the Pk-Fk relations between the loan_application table and matching dependent columns still need to be reapplied. 

I want to redo all of the coding to incorporate more complexity in the model, based on around ABS lodgement numbers for the month.  

I'll have to write up and cross reference this in the data generating python file and then run an INSERT script into the aggre_db. 

10/07/2025
Organization_table Architecture: 
- dropped organization_active from table as it was redundant given data scenario: the scope is only going to be with active. 


12/07/2025
- deep dove into some data scenarios to improve the scenario that the data is being generated from. It has moved from a generic financial product scenario
to a more specific mortgage finance based scenario. 

Data from the ABS loan commitments was broken down in order for an analysis of what new variables will need to be accounted for in the data scenario. In this instance, 
the loan types, again narrowing in on an industry, and ensuring that these loan types, as well as client types, are reflected in the data. 

This has meant a complete reordering of the data itself, and now has necessitated partial generations of data sets in order to reflect the different types of loans and clients as  
ratios of the total number of loan commitments from December 2024 to March 2025. 

This has been well-documented in the faker Python file. 

That said, the remaining tasks that have been left in this project are relatively easy to do:  generate data, insert data, extract data, and visualise data. 

In a way, this represents a culmination of efforts from the past 3 months and demonstrates my growing confidence and knowledge as a data analyst. 

24/07/2025
Data to be generated is based upon Data Connective Scenario Source and Assumptions. The logic, proportions etc. are all there and ready to be utilized for data generation. 

The next two things are this: 
Generate a new product table. 118 rows of variable and 2 fixed products. 

Generate the categories of loan-applications by: Accepted, Dropout and Rejected N% from aforementioned data source and ensure they are proportioned against the products of 
variable and fixed. 

The data in the loan application table will have to be generated piece-meal by category. 
Refer to notebook for structure. 

25/07/2025
Created a combine-CSV-Python-file that runs a concatenation pandas method. This is to join together the categorized product and loan_application rows in anticipation of 
inserting in the aggre db. 

product csv file error: left on purpose are two rows where the product_id keys are identical. I need this to simulate real-world errors where I can fix them. E.g. during an ETL 
process. 

26/07/2025
Produce loan_application data based upon loan_application data, combine it, and then insert all data into Maria DB

Clients and loan applications created. However, regarding the loan application data, it is only for approved. Rejected and drop out loan applications will need to be drawn up separately. 

SIGNIFICANT program CHANGE. 
Due to the scenario of this being data for a brokage aggregator, dropout and rejected rates are being dropped from the data scenario. 
The reason being is that this is based on the revenue for an aggregator and revenue is only realized once a mortgage is committed and or settled. 

27/07/2025
Changed mind: will be adding drop and rejected. I need it for comparative and churn purposes, especially churn, as this will show: 
A. lost potential business and establishing if there is some correlation with seasons etc. 
B. the CTC - the cost to acquire a customer. 

The structure for this has been completed and the data to be generated. That being said, there is the dilemma of the client ids. That there are not generated for the purposes
of the other loan application categories of rejected or dropout. That being said, I am loading into the data scenario business provisions for the Australian privacy act (APP11)
 and RGA 273 - Mortgage  brokers best interests duty - outlines that unless there is a legitimate purpose, retention must cease of client information. 
There is a provision that suggests, either way, that data should be retained for auditing purposes. However, I would argue, that this can be with the depersonification of the loan
application data itself. 

I think such considerations are worth baking into the data scenario as they demonstrate the wider legal and ethical frameworks that data analysts are expected to navigate. Therefore,
demonstrating even a cursory understanding of such an environment would look very good.  

They have been labelled categorically according to their start position. E.g. first home loan app rejected has a start id value of 127555 in the excel source. This
number has been utilized in the app_client_id field for categorization purposes. 

28/07/2025
Insert all data into maria db via aggre_db_run_SQL_script in python sql folder. 
Tables to insert: 
user, organization, marketing, product, clients, and loan application tables. 
These tables are located in the aggre_db_python folder. 

Inserting data from csv files: updated_product_table_completed, updated_marketing_table, updated_user_table, and clients_table_completed 
this had mixed results. 

Mixed results where data_types haven't been effectively inserted from CSV files. This will need to be investigated. One of the easiest fixes, for example, 
involved simply changing the structure of the formatting for a date column from dd-mm-yyyy to yyyy-mm-dd. Other issues might be a little more sophisticated and
involve dependencies. For example, they may involve foreign key constraints between an existing data in a table and another table that has received new data
and the rows haven't been entered entirely correct. 

29/07/2025. 
Refer to above entry and investigate why the values weren't successfully inserted. 
There were some data type and column value issues that have since been rectified. 

31/07/2025
Issue from the 29/07/2025 occurred again where, because of ENUM format on the marketing_channel column, values from the updated_marketing_table weren't 
able to be inserted into the column in Aggre_DB/Maria DB. 

Of note, this has been a repeated issue: that data type values do not match the columns that are being selected for upload query scripts in python. Interesting. 
String issue: VAR255 on column marketing-id had limitations around special characters like hyphens. Hyphens removed from Excel. 

Significant limitations with loan_application: rows that have either drop or rejected statuses for rows have identical client ids. From a scenario perspective, 
this was deemed acceptable as the client information wasn't retained due to the Australian Privacy Act. Read: it was no longer, arguably, permissible for the brokers or lenders
to retain the information as the application was rejected and or dropped. 
Unfortunately, this scenario crafting clashes with the pk and fk pairing between the loan_application and client tables. 

Arguably, seeing as from a process perspective, values are to be extracted from SQL and transformed elsewhere, such a structural dependency was probably excessive from a design
point of view. Now I have to undo this in order to upload all 200k+ rows of data from the loan_applicationallstatus csv file. 

Second big architectural shift: all pk-fk relationships inside of Aggre.db on the loan_application table have been dropped as connections between tables, from my 
professional experience, are generally created as constructs in queries in visualization software like Excel or Power BI. Not SQL databases. 

On a data architecture point of view, at the moment, the aggre_db is just a store of data. It doesn't have relationships mapped. And moving forward, as a structural 
feature I'll be keeping it as I want to store as MANY rows of data as I can. It appears that being too stringent with keys can be counter-productive in pursuing this 
strategy. 

Moreover, again going off experience, I haven't seen data that neatly stored. 

That said, all the data is now in the database ready for the rest of the data scenario. 

10/08/2025 
Data extracted from SQL, requires transformation in Python before being imported into Power BI for visualization. 
Also of concern that requires attention is the file architecture of the project. It needs to be consolidated, a directory created, and the dependencies between
the different files, from python data generating files to SQL handling files, properly catalogued and documented. 

This is so I can propose my value as a data analyst on a forum like GitHub. Without documentation explaining how everything relates together and why, it 
would be self-defeating. Moreover, I would need to be clear where I have completed the files themselves and where Chat GPT has come on. 

I have very consciously being googling and trying to ween myself off Chat GPT as I found using it too much would mean I would invariably treat it as a crutch. 

For the time being and for next time, I have created an aggre_2 folder where I have stored all of the files that are related to the second iteration of 
The aggregator data scenario.  
