import os
import pandas as pd
import numpy as np


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\clean_data\\data'
os.chdir(data_dir)

airlines = pd.read_csv('airlines_final.csv')

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins=label_ranges,
                               labels=label_names)

# Create mappings and replace
mappings = {'Monday': 'weekday', 'Tuesday': 'weekday',
            'Wednesday': 'weekday', 'Thursday': 'weekday',
            'Friday': 'weekday', 'Saturday': 'weekend',
            'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)
