import pandas as pd
import matplotlib.pyplot as plt
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_plt'
os.chdir(data_dir)

medals = pd.read_csv(
    'medals_by_country_2016.csv',
    index_col=0)

fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals['Gold'])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label
ax.set_ylabel('Number of medals')

# plt.show()

# Save as a PNG file with 300 dpi
fig.savefig('my_figure_300dpi.png', dpi=300)

# Set figure dimensions and save as a PNG
fig.set_size_inches([3, 5])
fig.savefig('figure_3_5.png')

fig.set_size_inches([5, 3])
fig.savefig('figure_5_3.png')
