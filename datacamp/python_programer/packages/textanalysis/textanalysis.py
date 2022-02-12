home_path = 'C:/Users/tiagog/Documents/curso-python/datacamp'
path_to_file = f'{home_path}/python_programer/packages/'


def count_words(filepath, words_list):

    # Open the text file
    filepath = path_to_file + filepath
    with open(filepath) as file:
        text = file.read()

    n = 0
    for word in text.split():
        # Count the number of times the words in the list appear
        if word.lower() in words_list:
            n += 1

    return n
