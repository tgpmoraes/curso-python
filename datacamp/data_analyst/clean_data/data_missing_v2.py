import pandas as pd
import bankingDS


banking = pd.DataFrame(bankingDS.banking_missing_values2)
banking.columns = bankingDS.banking_missing_columns2

# Print number of missing values in banking
print(banking.isna().sum())

# Drop missing values of cust_id
banking_fullid = banking.dropna(subset=['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount': acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())
