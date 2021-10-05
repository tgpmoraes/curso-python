import pandas as pd
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\data_mani_pandas'
os.chdir(data_dir)

temperatures = pd.read_csv('city_temperature.csv').drop(
    labels=['Region', 'State'],
    axis='columns')

temperatures['date'] = temperatures[
    (temperatures['Year'] > 1000) &
    (temperatures['Month'] > 0) &
    (temperatures['Day'] > 0)].apply(
    lambda row: pd.to_datetime(
        str(row.Year) + '-' +
        str(row.Month) + '-' +
        str(row.Day),
        format='%Y-%m-%d'), axis=1
)

temperatures[
    (temperatures['Year'] >= 2000) &
    (temperatures['Year'] < 2014)].to_csv('temperature_clean.csv')

# temperatures = pd.read_csv('temperature_clean.csv')

# Look at temperatures
# print(temperatures)

# Index temperatures by city
# temperatures_ind = temperatures.set_index('City')

# Look at temperatures_ind
# print(temperatures_ind)

# Reset the index, keeping its contents
# print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
# print(temperatures_ind.reset_index(drop=True))

# Make a list of cities to subset on
# cities = ["Moscow", "Yerevan"]

# Subset temperatures using square brackets
# print(temperatures[temperatures['City'].isin(cities)])

# Subset temperatures_ind using .loc[]
# print(temperatures_ind.loc[cities])

# Index temperatures by country & city
# temperatures_ind = temperatures.set_index(['Country', 'City'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
# rows_to_keep = [('Brazil', 'Rio de Janeiro'), ('Pakistan', 'Islamabad')]

# Subset for rows to keep
# print(temperatures_ind.loc[rows_to_keep])

# Sort temperatures_ind by index values
# print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
# print(temperatures_ind.sort_index(level='City'))

# Sort temperatures_ind by country then descending city
# print(temperatures_ind.sort_index(
#     level=['Country', 'City'],
#     ascending=[True, False]))
