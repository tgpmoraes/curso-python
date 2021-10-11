import pandas as pd
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\join_data'
os.chdir(data_dir)

sp500 = pd.read_csv('S&P500.csv')

sp500.rename(
    columns={
        'Date': 'date',
        'Returns': 'returns'},
    inplace=True
)

gdp = pd.read_csv('WorldBank_GDP.csv').drop(
    labels=['Country Code', 'Indicator Name'],
    axis='columns'
)

gdp.rename(
    columns={
        'Country Name': 'Country Name',
        'Year': 'year',
        'GDP': 'gdp'},
    inplace=True
)

# Use merge_ordered() to merge gdp and sp500 on year and date
# gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date',
#  how='left')

# Print gdp_sp500
# print(gdp_sp500)

# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date',
                             how='left', fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp', 'returns']]

# Print gdp_returns correlation
print(gdp_returns.corr())
