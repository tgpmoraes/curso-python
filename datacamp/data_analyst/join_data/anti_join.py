import pandas as pd
import streaming_ds


employees = pd.DataFrame(streaming_ds.employee,
                         columns=streaming_ds.emp_col)
top_cust = pd.DataFrame(streaming_ds.top_cust,
                        columns=streaming_ds.top_cust_col)


# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid',
                            how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])
