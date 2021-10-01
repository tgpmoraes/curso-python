# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv(
    'datacamp/data_analyst/intro_ds/credit_records.csv'
)

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())

# Use .info() to inspect the DataFrame credit_records
print(credit_records.info())
