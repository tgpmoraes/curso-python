import pandas as pd
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\data_mani_pandas'
os.chdir(data_dir)

temperatures = pd.read_csv('temperature_clean.csv')
temperatures['date'] = pd.to_datetime(temperatures['date'], format='%Y-%m-%d')

# Index temperatures by country & city
# temperatures_ind = temperatures.set_index(['Country', 'City'])

# Sort the index of temperatures_ind
# temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
# print(temperatures_srt.loc['Pakistan':'Russia'])

# Try to subset rows from Lahore to Moscow
# print(temperatures_srt.loc['Islamabad':'Moscow'])

# Subset rows from Pakistan, Lahore to Russia, Moscow
# print(temperatures_srt.loc[('Pakistan', 'Islamabad'):('Russia', 'Moscow')])

# Subset rows from India, Hyderabad to Iraq, Baghdad
# print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad')])

# Subset columns from date to avg_temp_c
# print(temperatures_srt.loc[:, 'date':'AvgTemperature'])

# Subset in both directions at once
# print(temperatures_srt.loc[
# ('India', 'Hyderabad'):('Iraq', 'Baghdad'), 'date':'AvgTemperature'])

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
# temperatures_bool = temperatures[
#     (temperatures['date'] >= '2010-01-01') &
#     (temperatures['date'] <= '2011-12-31')]
# print(temperatures_bool)

# Set date as the index and sort the index
# temperatures_ind = temperatures.set_index('date').sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
# datacamp funciona
# print(temperatures_ind.loc['2010':'2011'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
# print(temperatures_ind.loc['2010-08':'2011-02'])

# Get 23rd row, 2nd column (index 22, 1)
# print(temperatures.iloc[22, 1])

# Use slicing to get the first 5 rows
# print(temperatures.iloc[:5, :])

# Use slicing to get columns 3 to 4
# print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
# print(temperatures.iloc[:5, 2:4])

# Add a year column to temperatures
temperatures['year'] = temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(
    'AvgTemperature',
    index=['Country', 'City'],
    columns='year')

# Subset for Egypt to India
print(temp_by_country_city_vs_year.loc['Egypt':'India'])

# Subset for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi')])

# Subset in both directions at once
print(temp_by_country_city_vs_year.loc[
    ('Egypt', 'Cairo'):('India', 'Delhi'), 2005:2010])

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean(axis='index')

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[
    mean_temp_by_year == temp_by_country_city_vs_year
    .mean(axis='index').max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[
    mean_temp_by_city == temp_by_country_city_vs_year
    .mean(axis='columns').min()])
