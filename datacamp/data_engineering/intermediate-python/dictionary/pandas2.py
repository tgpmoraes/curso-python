# Import cars data
import pandas as pd
home_path = 'C:/Users/tiagog/Documents/curso-python'
cars = pd.read_csv(
    f'{home_path}/datacamp/intermediate-python/dictionary/cars.csv',
    index_col=0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:7])

# Run in interactive mode
cars.loc['RU']
cars.iloc[4]

cars.loc[['RU']]
cars.iloc[[4]]

cars.loc[['RU', 'AUS']]
cars.iloc[[4, 1]]

# Print out observation for Japan as Pandas Series
print(cars.loc['JPN'])
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1, 6]])

# Run in interactive mode
cars.loc['IN', 'cars_per_cap']
cars.iloc[3, 0]

cars.loc[['IN', 'RU'], 'cars_per_cap']
cars.iloc[[3, 4], 0]

cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
cars.iloc[[3, 4], [0, 1]]

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Run in interactive mode
cars.loc[:, 'country']
cars.iloc[:, 1]

cars.loc[:, ['country', 'drives_right']]
cars.iloc[:, [1, 2]]

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])
print(cars.iloc[:, 1])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])
print(cars.iloc[:, [1]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
print(cars.iloc[:, [2, 1]])
