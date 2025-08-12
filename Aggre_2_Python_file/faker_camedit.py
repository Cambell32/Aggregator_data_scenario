#this file is for generating fake cvs files 
import pandas as pd
import uuid
import random
from faker import Faker
import datetime
from datetime import date


# Initialize Faker
fake = Faker()
end_date = datetime.date(2025, 3, 31)
start_date = datetime.date(2024, 12, 1)

def generate_table_csv(n):
   
   i = 255090
   data = []
   for i in range(i, i + n):
    def appLodgement():
            return fake.date_between_dates(date_start=start_date, date_end=end_date)

    def app_last_updated(date):
            return fake.date_between_dates(date_start=date, date_end=end_date)
    
    applodged = appLodgement() #this must be placed into the iterative loop otherwise, once the data is generated, its going to be repeated through the iterations. 
    data.append({
            'app_application_id': i,
            'app_client_id' : 255090, 
            'app_broker_id' :random.choice([1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	
            30,	31,	32,	33,	34,	35,	36,	37,	38,	39,	40,	41,	42,	43,	44,	45,	46,	47,	48,	49,	50,	51,	52,	53,	54,	55,	56,	57,	58,	59,	60
            ]),
            'app_lender_id' : random.choice([
            2,	3,	6,	9,	10,	11,	13,	14,	15,	16,	17,	19,	20,	22,	25,	26,	27,	28,	29,	31,	34,	35,	36,	40,
            ]),
            'app_status' : 'drop',
            'app_lodgement_date' : applodged,
            'app_amount_requested' : random.randint(500000, 4500000),
            'app_product_id' :random.randint(119,120),
            'app_marketing_id' :random.randint(1, 100),
            'app_last_updated' : app_last_updated(applodged) 
    })

 
   return pd.DataFrame(data)

# Generate the data
df_inactive = generate_table_csv(579)

# Save to CSV
csv_filename = "loan_application_investor_drop_fixed.csv"
df_inactive.to_csv(csv_filename, index=False)

print(f"CSV saved as: {'loan_application_investor_drop_fixed'}")


#.isoformat() this is used for date objects, will cause an error on strings. 
# random.choice([])
#fake.random_number(digits=11, fix_len=True) 

#pd.concat([file1,file2])


