# Import custom text_analyzer package
import text_analyzer


datacamp_tweet = ('Basic linear regression example.'
                  ' #DataCamp #DataScience #Python #sklearn')

# Create an instance of Document with datacamp_tweet
my_document = text_analyzer.Document(text=datacamp_tweet)

# Print the text attribute of the Document instance
print(my_document.word_counts.most_common(5))
