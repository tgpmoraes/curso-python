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

survey_data['Interested in Pets'] = survey_data['Pets'].apply(
    lambda pets: False if pets < 4 else True
)

survey_data['Likes Techno'] = survey_data['Techno'].apply(
    lambda techno: False if techno < 4 else True
)

survey_data['Parents Advice'] = survey_data['Parents Advice'].apply(
    lambda advice: 'Always' if advice == 5 else
    ('Often' if advice == 4 else
     ('Sometimes' if advice == 3 else
      ('Rarely' if advice == 2 else
       ('Never' if advice == 1 else advice)
       )
      )
     )
)

# Set the figure style to "dark"
sns.set_style('dark')

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno",
                data=survey_data, kind="bar",
                col='Gender')

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence",
      ylabel="% Who Like Techno")

# Show plot
plt.show()
