# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv(
    'datacamp/data_analyst/intro_ds/credit_records.csv'
)

# Select the column item from credit_records
# Use brackets and string notation
items = credit_records['item']

# Display the results
print(items)
