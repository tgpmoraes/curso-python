# Import cars data
import pandas as pd
# Import numpy, you'll need this
import numpy as np
home_path = 'C:/Users/tiagog/Documents/curso-python'
cars = pd.read_csv(
    f'{home_path}/datacamp/intermediate-python/dictionary/cars.csv',
    index_col=0)

np_iter = np.array([1, 2, 3, 4, 5])
# print(type(np_iter))

# for item in np.nditer(np_iter):
#     print(item)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print('{}: {}'.format(lab, row['cars_per_cap']))

# Code for loop that adds COUNTRY column
# for lab, row in cars.iterrows():
#     cars.loc[lab, 'COUNTRY'] = row['country'].upper()

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)
