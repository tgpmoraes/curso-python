import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_sns'
os.chdir(data_dir)
csv_filepath = 'young-people-survey-responses.csv'

# Create a DataFrame from csv file
survey_data = pd.read_csv(csv_filepath)

survey_data['Age Category'] = survey_data['Age'].apply(
    lambda age: 'Less than 21' if age < 21 else '21+'
)

survey_data['Interested in Math'] = survey_data['Mathematics'].apply(
    lambda maths: False if maths < 4 else True
)

# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender', y='Interested in Math',
            data=survey_data,
            kind='bar')

# Show plot
plt.show()
