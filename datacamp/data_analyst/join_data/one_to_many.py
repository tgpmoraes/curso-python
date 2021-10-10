import pandas as pd
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\join_data'
os.chdir(data_dir)

# n = 10  # every 10th line = 1% of the lines
# licenses = pd.read_csv('business-licenses.csv', header=0,
#                        skiprows=lambda i: i % n != 0).drop(
#     labels=['ID', 'LICENSE ID', 'SITE NUMBER', 'LEGAL NAME', 'CITY', 'STATE',
#             'PRECINCT', 'WARD PRECINCT', 'POLICE DISTRICT', 'LICENSE CODE',
#             'LICENSE DESCRIPTION', 'BUSINESS ACTIVITY ID',
#             'BUSINESS ACTIVITY',
#             'LICENSE NUMBER', 'APPLICATION TYPE', 'APPLICATION CREATED DATE',
#             'APPLICATION REQUIREMENTS COMPLETE', 'PAYMENT DATE',
#             'CONDITIONAL APPROVAL', 'LICENSE TERM START DATE',
#             'LICENSE TERM EXPIRATION DATE', 'LICENSE APPROVED FOR ISSUANCE',
#             'DATE ISSUED', 'LICENSE STATUS', 'LICENSE STATUS CHANGE DATE',
#             'SSA', 'LATITUDE', 'LONGITUDE', 'LOCATION', 'Community Areas',
#             'Historical Wards 2003-2015', 'Zip Codes', 'Census Tracts',
#             'Wards'],
#     axis='columns'
# )

licenses = pd.read_csv('licenses.csv')

biz_owners = pd.read_csv('business-owners.csv').drop(
    labels=['Legal Name', 'Owner Middle Initial', 'Suffix',
            'Legal Entity Owner'],
    axis='columns'
)

licenses.rename(columns={'ACCOUNT NUMBER': 'account'},
                inplace=True)
biz_owners.rename(columns={
    'Title': 'title',
    'Account Number': 'account'},
    inplace=True)

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners,
                                 on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg(
    {'account': 'count'})
# counted_df = licenses_owners.groupby('title')['account'].count()

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values('account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())
# print(counted_df.sort_values(ascending=False))
