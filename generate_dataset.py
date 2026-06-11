import pandas as pd
import numpy as np
import random
import os

os.makedirs("data", exist_ok=True)

cities = ["New York","Chicago","Dallas","Houston","Los Angeles"]

products = [
    "Laptop",
    "Phone",
    "Watch",
    "Shoes",
    "Headphones"
]

categories = [
    "Electronics",
    "Fashion",
    "Sports"
]

rows=[]

for i in range(1000):

    income=np.random.randint(20000,150000)
    spending=np.random.randint(1,100)
    tenure=np.random.randint(1,10)
    visits=np.random.randint(1,30)

    churn=1 if spending<30 and visits<5 else 0

    rows.append([
        i+1,
        f"Customer_{i+1}",
        np.random.randint(18,65),
        random.choice(["Male","Female"]),
        random.choice(cities),
        income,
        spending,
        tenure,
        visits,
        random.choice(products),
        random.choice(categories),
        np.random.randint(1,20),
        churn
    ])

cols=[
'customer_id',
'name',
'age',
'gender',
'city',
'income',
'spending_score',
'tenure',
'monthly_visits',
'favorite_product',
'favorite_category',
'purchase_frequency',
'churn'
]

df=pd.DataFrame(rows,columns=cols)

df.to_csv("data/customers.csv",index=False)

print("Dataset Generated Successfully")