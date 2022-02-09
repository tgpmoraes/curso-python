# Import custom text_analyzer package
import text_analyzer


home_path = 'C:/Users/tiagog/Documents/curso-python/datacamp/python_programer'
file_path = f'{home_path}/software_engineering/document_tweets.txt'
with open(file_path, encoding='UTF-8') as input:
    datacamp_tweets = input.read()
input.close()

# Create instance of document
my_doc = text_analyzer.Document(datacamp_tweets)

# Run help on my_doc's plot method
help(my_doc.plot_counts)

# Plot the word_counts of my_doc
my_doc.plot_counts()
