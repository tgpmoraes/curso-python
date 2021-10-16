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

# Add a bar for the rowing "Height" column mean/std
ax.bar(
    "Rowing",
    mens_rowing['Height'].mean(),
    yerr=mens_rowing['Height'].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar(
    "Gymnastics",
    mens_gymnastics['Height'].mean(),
    yerr=mens_gymnastics['Height'].std())

# Label the y-axis
ax.set_ylabel("Height (cm)")

plt.show()
