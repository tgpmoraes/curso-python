# Import custom text_analyzer package
import text_analyzer


home_path = 'C:/Users/tiagog/Documents/curso-python/datacamp/python_programer'
file_path = f'{home_path}/software_engineering/document_tweets.txt'
with open(file_path, encoding='UTF-8') as input:
    datacamp_tweets = input.read()
input.close()


# Create a SocialMedia instance with datacamp_tweets
dc_tweets = text_analyzer.SocialMedia(text=datacamp_tweets)

# Print the top five most most mentioned users
print(dc_tweets.mention_counts.most_common(5))

# Plot the most used hashtags
text_analyzer.plot_counter(dc_tweets.hashtag_counts)
