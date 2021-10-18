import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_sns'
os.chdir(data_dir)
csv_filepath = 'mpg.csv'

# Create a DataFrame from csv file
mpg = pd.read_csv(csv_filepath)

# Create scatter plot of horsepower vs. mpg
sns.relplot(x='horsepower', y='mpg',
            data=mpg,
            kind='scatter',
            size='cylinders',
            hue='cylinders')

# Show plot
plt.show()
