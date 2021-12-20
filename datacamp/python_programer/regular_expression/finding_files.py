import os
import pandas as pd
import re


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\regular_expression'
os.chdir(data_dir)

tweets = pd.read_csv('short_tweets.csv')

sentiment_analysis = tweets[tweets['id'].isin(
    [1468017259, 1468018354])]['text']

# Write a regex to match text file name
regex = r"^[aeiouAEIOU]{2,3}.+txt"

for text in sentiment_analysis:
    # Find all matches of the regex
    print(re.findall(regex, text))

    # Replace all matches with empty string
    print(re.sub(regex, "", text))
