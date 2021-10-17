import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_sns'
os.chdir(data_dir)
csv_filepath = 'student-alcohol-consumption.csv'

# Create a DataFrame from csv file
student_data = pd.read_csv(csv_filepath)

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(
    x="school",
    data=student_data,
    hue="location",
    palette=palette_colors)

# Display plot
plt.show()
