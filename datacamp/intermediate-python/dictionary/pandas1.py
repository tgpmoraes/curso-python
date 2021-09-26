# Import pandas as pd
import pandas as pd


names = ['United States', 'Australia', 'Japan',
         'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

home_path = 'C:/Users/tiagog/Documents/curso-python'
cars.to_csv(f'{home_path}/datacamp/intermediate-python/dictionary/cars.csv',
            encoding='utf=8')

# Import the cars.csv data: cars
cars = pd.read_csv(
    f'{home_path}/datacamp/intermediate-python/dictionary/cars.csv',
    index_col=0)

# Print out cars
print(cars)
