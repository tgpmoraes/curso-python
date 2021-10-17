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

region = countries_data['Region'].str.strip().values.tolist()

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()
