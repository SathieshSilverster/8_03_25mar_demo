import numpy as np
import pandas as pd
import random
from faker import Faker

fake=Faker()
# Increase dataset size to 300,000 rows and add more than 15 columns
num_rows = 300000  # 3 lakh rows

# Create a larger dataset with additional columnsa 
data_large = {
    "ID": np.arange(1, num_rows + 1),
    "Name": [fake.name() for _ in range(num_rows)],
    "Age": np.random.randint(18, 65, num_rows),
    "City": [fake.city() for _ in range(num_rows)],
    "Salary": np.random.randint(30000, 150000, num_rows),
    "Joining_Date": [fake.date_this_decade() for _ in range(num_rows)],
    "Department": np.random.choice(["IT", "HR", "Finance", "Marketing", "Operations"], num_rows),
    "Experience_Years": np.random.randint(0, 40, num_rows),
    "Rating": np.round(np.random.uniform(1.0, 5.0, num_rows), 1),
    "Gender": np.random.choice(["Male", "Female", "Other"], num_rows),
    "Marital_Status": np.random.choice(["Single", "Married", "Divorced"], num_rows),
    "Country": [fake.country() for _ in range(num_rows)],
    "Email": [fake.email() for _ in range(num_rows)],
    "Phone": [fake.phone_number() for _ in range(num_rows)],
    "Product_Purchase": np.random.choice(["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch"], num_rows),
    "Purchase_Amount": np.round(np.random.uniform(100, 5000, num_rows), 2),
    "Last_Login": [fake.date_time_this_year() for _ in range(num_rows)],
    "Subscription_Status": np.random.choice(["Active", "Inactive", "Cancelled"], num_rows),
    "Feedback_Score": np.round(np.random.uniform(1, 10, num_rows), 1),
    "Discount_Applied": np.random.choice(["Yes", "No"], num_rows)
}

# Convert to DataFrame
df_large = pd.DataFrame(data_large)

# Save the dataset to CSV
large_file_path = "D:\\powe_BI\\samples\\large_dataset_300k.csv"
df_large.to_csv(large_file_path, index=False)

# Provide file path
large_file_path
