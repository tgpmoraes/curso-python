# Import cars data
import pandas as pd
# Import numpy, you'll need this
import numpy as np
home_path = 'C:/Users/tiagog/Documents/curso-python'
cars = pd.read_csv(
    f'{home_path}/datacamp/intermediate-python/dictionary/cars.csv',
    index_col=0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)

# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars[cars['cars_per_cap'] > 500]

# Print car_maniac
print(car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and(cars['cars_per_cap'] > 100,
                             cars['cars_per_cap'] < 500)]

# Print medium
print(medium)
