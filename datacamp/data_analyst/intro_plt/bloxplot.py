import pandas as pd
import matplotlib.pyplot as plt
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_plt'
os.chdir(data_dir)

medalist_weights = pd.read_csv(
    'summer2016.csv',
    index_col=0)

mens_rowing = medalist_weights[medalist_weights['Sport'] == 'Rowing']
mens_gymnastics = medalist_weights[medalist_weights['Sport'] == 'Gymnastics']

fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing['Height'], mens_gymnastics['Height']])

# Add x-axis tick labels:
ax.set_xticklabels(['Rowing', 'Gymnastics'])

# Add a y-axis label
ax.set_ylabel('Height (cm)')

plt.show()
