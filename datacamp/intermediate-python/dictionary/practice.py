import pandas as pd
import numpy as np


home_path = 'C:/Users/tiagog/Documents/curso-python'
# Import the datacamp.csv data: datacamp
datacamp = pd.read_csv(
    f'{home_path}/datacamp/intermediate-python/dictionary/datacamp.csv',
    index_col=0)

# Print out datacamp
# print(datacamp[datacamp['chapter'] < 3])
print(datacamp.iloc[[0], :])

sales = pd.read_csv(
    f'{home_path}/datacamp/intermediate-python/dictionary/sales.csv'
)

pick = np.logical_or(sales['product'] == 'B',
                     sales['sold'] < 100)

# print(sales[pick])

fifa_wc_results = pd.read_csv(
    f'{home_path}/datacamp/intermediate-python/dictionary/fifa_wc_results.csv'
)

# print(fifa_wc_results.iloc[:, 4])
