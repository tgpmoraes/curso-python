import os
import pandas as pd


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\regular_expression'
os.chdir(data_dir)

movies = pd.read_csv('short_movies.csv')

movies = movies[(movies['html'] == 11636) &
                (movies['sent id'].isin([12, 13]))]['text']

for movie in movies:
    try:
        # Find the first occurrence of word
        print(movie.index('money', 12, 51))
    except ValueError:
        print("substring not found")
