# Import Matplotlib and Seaborn
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_sns'
os.chdir(data_dir)

countries_data = pd.read_csv(
    'countries-of-the-world.csv',
    decimal=',',
    quotechar='"')

gdp = countries_data['GDP ($ per capita)'].values.tolist()
phones = countries_data['Phones (per 1000)'].values.tolist()
percent_literate = countries_data['Literacy (%)'] \
    .values.tolist()

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()
