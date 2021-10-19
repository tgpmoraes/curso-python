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

# List of categories from lowest to highest
study_time_order = ["<2 hours",
                    "2 to 5 hours",
                    "5 to 10 hours",
                    ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x='study_time', y='G3',
            data=student_data,
            kind='box',
            order=study_time_order)

# Show plot
plt.show()
