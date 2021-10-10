import pandas as pd
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\join_data'
os.chdir(data_dir)

ward = pd.read_csv('ward-offices.csv').drop(
    labels=['CITY', 'STATE', 'WARD PHONE', 'WARD FAX', 'EMAIL', 'WEBSITE',
            'LOCATION', 'CITY HALL ADDRESS', 'CITY HALL CITY',
            'CITY HALL STATE', 'CITY HALL ZIPCODE', 'CITY HALL PHONE',
            'Community Areas', 'Zip Codes', 'Census Tracts', 'Wards',
            'Historical Wards 2003-2015', 'Boundaries - ZIP Codes'],
    axis='columns'
)

census = pd.read_csv('censusData.csv').drop(
    labels=['PERCENT OF HOUSING CROWDED',  'PERCENT HOUSEHOLDS BELOW POVERTY',
            'PERCENT AGED 16+ UNEMPLOYED',
            'PERCENT AGED 25+ WITHOUT HIGH SCHOOL DIPLOMA',
            'PERCENT AGED UNDER 18 OR OVER 64',  'PER CAPITA INCOME ',
            'HARDSHIP INDEX',  'NORM POP', 'NORM INCCAP'],
    axis='columns'
)

ward_census = ward.merge(census, on='WARD')

print(ward_census.head())
