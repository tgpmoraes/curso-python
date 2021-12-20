import os
import pandas as pd
import re


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\regular_expression'
os.chdir(data_dir)

tweets = pd.read_csv('short_tweets.csv')

sentiment_analysis = tweets['text']

urls = []
users = []

for tweet in sentiment_analysis:
    # Write regex to match http links and print out result
    url = re.findall(r"https?\W+\w*.?\w+.\w+", tweet)
    if (len(url) > 0):
        urls.append(url)

    # Write regex to match user mentions and print out result
    user = re.findall(r"@\w+\d*", tweet)
    if (len(user) > 0):
        users.append(user)

print(urls[:5])
print(users[:5])
