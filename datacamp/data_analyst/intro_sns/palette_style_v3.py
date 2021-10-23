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

# Set the style to "darkgrid"
sns.set_style('darkgrid')

# Set a custom color palette
custom_palette = ["#39A7D0", "#36ADA4"]
sns.set_palette(custom_palette)

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age",
            data=survey_data, kind="box")

# Show plot
plt.show()
