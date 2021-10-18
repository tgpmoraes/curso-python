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

# Change to make subplots based on study time
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            row='study_time')

# Show plot
plt.show()
