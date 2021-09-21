from pandas_mysql import get_connection, extract_table_to_pandas


# Complete the transformation function
def transform_avg_rating(rating_data):
    # Group by course_id and extract average rating per course
    avg_rating = rating_data.groupby('release_year').rental_rate.mean()
    # Return sorted average ratings per course
    sort_rating = avg_rating.sort_values(ascending=False).reset_index()
    return sort_rating


# The transformation should fill in the missing values
def transform_fill_programming_language(rating_data):
    imputed = rating_data.fillna({"original_language_id": "en"})
    return imputed


db_engines = get_connection('sakila')

rating_data = extract_table_to_pandas('film', db_engines)

# Use transform_avg_rating on the extracted data and print results
avg_rating_data = transform_avg_rating(rating_data)
print(avg_rating_data)

# Print out the number of missing values per column
print(rating_data.isnull().sum())

transformed = transform_fill_programming_language(rating_data)

# Print out the number of missing values per column of transformed
print(transformed.isnull().sum())
