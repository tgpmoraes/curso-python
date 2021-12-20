import os
import pandas as pd
import re


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\regular_expression'
os.chdir(data_dir)

tweets = pd.read_csv('short_tweets.csv')

sentiment_analysis = tweets['text']

date_list = []

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
    d1 = re.findall(r"\d{1,2}\s\w+\s\w+", date)
    d2 = re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date)
    d3 = re.findall(r"\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}", date)
    if len(d1) > 0:
        date_list.append(d1)
    if len(d2) > 0:
        date_list.append(d2)
    if len(d3) > 0:
        date_list.append(d3)

print(date_list[:5])
