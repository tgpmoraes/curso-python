import os
import pandas as pd


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\regular_expression'
os.chdir(data_dir)

movies = pd.read_csv('short_movies.csv')

movies = movies[(movies['html'] == 15448) &
                (movies['sent id'].isin([16, 17, 18]))]['text']

for movie in movies:
    # If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.count("actor") == 2:
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences with one
        print(movie.replace("actor actor actor", "actor"))
