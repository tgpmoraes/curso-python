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

survey_data['Feels Lonely'] = survey_data['Loneliness'].apply(
    lambda alone: False if alone < 4 else True
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

survey_data['Number of Siblings'] = survey_data['Siblings'].apply(
    lambda siblings: '0' if siblings == 0 else
    ('1 - 2' if siblings < 3 else
     ('3+' if siblings >= 3 else siblings)
     )
)

# Set the context to "paper"
sns.set_context('paper')
# Change the context to "notebook"
# sns.set_context("notebook")
# Change the context to "talk"
# sns.set_context("talk")
# Change the context to "poster"
# sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()
