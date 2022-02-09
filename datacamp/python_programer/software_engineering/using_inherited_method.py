# Import custom text_analyzer package
import text_analyzer


home_path = 'C:/Users/tiagog/Documents/curso-python/datacamp/python_programer'
file_path = f'{home_path}/software_engineering/document_tweets.txt'
with open(file_path, encoding='UTF-8') as input:
    datacamp_tweets = input.read()
input.close()

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(text=datacamp_tweets)

# Plot the most used hashtags in the tweets
my_tweets.plot_counts('hashtag_counts')
