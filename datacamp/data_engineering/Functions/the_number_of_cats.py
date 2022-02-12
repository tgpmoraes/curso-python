# Open "alice.txt" and assign the file to "file"
home_path = 'C:/Users/tiagog/Documents/curso-python/datacamp'
file_path = f'{home_path}/data_engineering/Functions/alice.txt'
with open(file_path, encoding='UTF-8') as file:
    text = file.read()

n = 0
for word in text.split():
    if word.lower() in ['cat', 'cats']:
        n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))
