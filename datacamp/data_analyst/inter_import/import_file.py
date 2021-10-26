import os
from urllib.request import urlretrieve
import pandas as pd


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_import\\data'
os.chdir(data_dir)

# Assign url of file: url
url = '''
https://s3.amazonaws.com/assets.datacamp.com/\
production/course_1606/datasets/winequality-red.csv'''

# Save file locally
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())
