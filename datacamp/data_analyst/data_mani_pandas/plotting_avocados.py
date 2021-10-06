import pandas as pd
import os
import matplotlib.pyplot as plt


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\data_mani_pandas'
os.chdir(data_dir)

avocados = pd.read_csv('avocado.csv', index_col=0).drop(
    labels=['Total Volume', '4046', '4225', '4770', 'Total Bags', 'region'],
    axis='columns'
)

avocados = avocados.melt(id_vars=["date", "avg_price", 'type', 'year'],
                         var_name="size",
                         value_name="nb_sold")
# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
# nb_sold_by_size.plot(kind='bar')

# Show the plot
# plt.show()

# Get the total number of avocados sold on each date
# nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
# nb_sold_by_date.plot(x='date', y='nb_sold', kind='line')

# Show the plot
# plt.show()

# Scatter plot of nb_sold vs avg_price with title
# avocados.plot(x='nb_sold',
#               y='avg_price',
#               kind='scatter',
#               title='Number of avocados sold vs. average price')

# Show the plot
# plt.show()

# Modify bins to 20
avocados[
    avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Modify bins to 20
avocados[
    avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()
