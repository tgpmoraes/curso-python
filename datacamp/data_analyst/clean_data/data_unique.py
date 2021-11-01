import os
import pandas as pd


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\clean_data\\data'
os.chdir(data_dir)

airlines = pd.read_csv('airlines_final.csv')

categories = pd.DataFrame([['Clean', 'Neutral', 'Very satisfied'],
                           ['Average', 'Very safe', 'Neutral'],
                           ['Somewhat clean', 'Somewhat safe',
                               'Somewhat satisfied'],
                           ['Somewhat dirty', 'Very unsafe',
                               'Somewhat unsatisfied'],
                           ['Dirty', 'Somewhat unsafe', 'Very unsatisfied']])

categories.columns = ['cleanliness', 'safety', 'satisfaction']

# Print categories DataFrame
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])
