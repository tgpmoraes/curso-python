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

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x='acceleration', y='mpg',
            data=mpg,
            kind='scatter',
            style='origin',
            hue='origin')

# Show plot
plt.show()
