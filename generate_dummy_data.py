# generate_dummy_data.py
import pandas as pd
import numpy as np

# Create a mock legacy dataset with intentional governance issues
data = {
    'Transaction_ID': [f'TXN_{i}' for i in range(100)] + ['TXN_50', 'TXN_51'], # Added duplicates
    'Account_Number': np.random.randint(10000, 99999, 102),
    'Transaction_Amount': np.random.uniform(10.0, 5000.0, 102),
    'Branch_Code': ['BR_01', 'BR_02', 'BR_03', None] * 25 + ['BR_01', 'BR_02'], # Missing values
    'Customer_Type': ['Retail', 'Corporate', 'SME', 'Retail', np.nan, 'Retail'] * 17, # Missing values
    'Status': ['Completed'] * 100 + ['Failed', 'Pending']
}

df = pd.DataFrame(data)

# Injecting some random NaNs into Transaction_Amount to simulate dirty data
df.loc[5:15, 'Transaction_Amount'] = np.nan

df.to_csv('legacy_financial_data.csv', index=False)
print("Mock legacy data generated: legacy_financial_data.csv")
