from text_analyzer import Document


home_path = 'C:/Users/tiagog/Documents/curso-python/datacamp/python_programer'
file_path = f'{home_path}/software_engineering/document_tweets.txt'
with open(file_path, encoding='UTF-8') as input:
    document_tweets = input.read()
input.close()

# create a new document instance from datacamp_tweets
datacamp_doc = Document(text=document_tweets)

# print the first 5 tokens from datacamp_doc
print(datacamp_doc.tokens[:5])

# print the top 5 most used words in datacamp_doc
print(datacamp_doc.word_counts.most_common(5))
