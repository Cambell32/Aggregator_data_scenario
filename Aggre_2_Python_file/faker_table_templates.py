#File that contains templates for data generation.

"""
---Scenario data generation loop components and notes --- 
These are to be used in the faker_camedit file for data generation. 
                Loan application 
For a break down of data to be generated for the approved / committed loans plug in the data from 
Data Connective Scenario Source: C:\Users\cambe\Desktop\Data Analytics\Data Analyst Scenarios\Connective SaaS scenario\Home Loans_ Australian Mortgage Debt Statistics (2025)_files

Note: for some columns, they are going to portions. E.g. the rate field is going be a variable rate of 98% for the total number
of approved loans. 
These inputs will need to be added for each client type and other dependent tables of the data for the scenario. 


app_lodgement and app_last_updated fields handling: 
Because of the iterative nature of the loop, fake date data has to be generated for each loop as, the app_last_update function
needs the appLodgement for start date parameter in order to ensure date consistency for these two date columns. 

end_date = datetime.date(2025, 3, 31)
start_date = datetime.date(2024, 12, 1)

def appLodgement():
    return fake.date_between_dates(date_start=start_date, date_end=end_date)

def app_last_updated(date):
    return fake.date_between_dates(date_start=date, date_end=end_date)

applodged = appLodgement() - this must be placed into the iterative loop otherwise, once the data is generated, its going to be repeated through the iterations. 

'app_application_id' : i ,
            'app_client_id' : random.randint(0,15000), 
            'app_broker_id' :random.choice([1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	
            30,	31,	32,	33,	34,	35,	36,	37,	38,	39,	40,	41,	42,	43,	44,	45,	46,	47,	48,	49,	50,	51,	52,	53,	54,	55,	56,	57,	58,	59,	60

            ]),
            'app_lender_id' : random.choice([
            2,	3,	6,	9,	10,	11,	13,	14,	15,	16,	17,	19,	20,	22,	25,	26,	27,	28,	29,	31,	34,	35,	36,	40,

            ]),
            'app_status' : random.choice(['approved']),
            'app_lodgement_date' : applodged,
            'app_amount_requested' : random.randint(500000, 4500000),
            'app_product_id' :random.randint(1,120),
            'app_marketing_id' :random.randint(1, 100),
            'app_last_updated' : app_last_updated(applodged) 


                           --- Product table data generator ---
'product_id': i,
'product_type': 'variable',
'product_organization_id':random.choice([1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,
	25,	26,	27,	28,	29,	30,	31,	32,	33,	34,	35,	36,	37,	38,	39,	40,	41,	42,	43,	44,	45,	46,	47,	48,	49,	50,	51,	52,	53,	54,
	55,	56,	57,	58,	59,	60,	61,	62,	63,	64,	65,	66,	67,	68,	69,	70,	71,	72,	73,	74,	75,	76,	77,	78,	79,	80,	81,	82,	83,	84,	85,	86,
    87,	88,	89,	90,	91,	92,	93,	94,	95,	96,	97,	98,	99,	100,
    101,	102,	103,	104,	105,	106,	107,	108,	109,	110,	111,	112,	113,	114,	115,	116,	117,	118,	119,	120
])

                            --- Client table data generator ---
        client_type is the most sensitive to accuracy and so the Connective Data scenario should be heavily referenced when generating  client type data.

        
"client_id": i,
            "client_name": fake.name(),
            "client_dob": fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat(),
            "client_number": fake.random_number(digits=11, fix_len=True),
            "client_type": 'investor', first-homer-buyer, non-first-home-buyer, investor
            "client_created_by": random.randint(1, 80) 
"""

""" 

Previous iteration of columns for data iteration. 


Client CSV file building

  "client_id": str(uuid.uuid4()),
            "client_name": fake.name(),
            "client_dob": fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat()
            "client_number": fake.random_number(digits=11, fix_len=True),
            "client_type": fake.random(['firsthome','nonfirsthome','investor']),
            "client_email": fake.email()
            "client_created_by": random.randint(1,80)

    Product CSV file building
   "product_id": count+ 1,
            "product_type": random.choice(["standard","competitive","premium]"]),
            "product_organization_id": random.choice([2,4,9,5,6,20,8,13,11,12,]),
            "product_lender_id" : random.choice([3,17,34,15,56])

    User CSV file building
      "user_id": user_id,
         "user_name": fake.name(),
         "user_email": fake.email(),
         "user_role": random.choice(['Admin','Broker','Lender']),
         
         "user_created_at": fake.date_between(start_date= date(2018, 1, 1), end_date=date(2025, 12, 31))

    Marketing CSV file building
     "marketing_id": i,
      "marketing_name": random.choice(["Broker-Strategy-4","Broker-Strategy-5","Broker-Strategy-3","Broker-Strategy-6","Broker-Strategy-7"]),
      "marketing_channel" : random.choice(["Linkedin","Google-SEO","Facebook","Jobboard","Upsale-by-lender"])
"""


"""
 "client_id": i,
            "client_name": fake.name(),
            "client_dob": fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat(),
            "client_number": fake.random_number(digits=11, fix_len=True),
            "client_email": fake.email(),
            "client_created_by": random.choice([2,4,5,6,11,14,15,19,23,25,29,32,35,39,42,44,45,48,50,51,52,54,55,56,64,65,67,68,70,73,75,77,78])
"""