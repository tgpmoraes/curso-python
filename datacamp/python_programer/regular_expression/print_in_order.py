wikipedia_article = ("In computer science, artificial intelligence (AI), "
                     "sometimes called machine intelligence, is intelligence "
                     "demonstrated by machines, in contrast to the natural "
                     "intelligence displayed by humans and animals.")

my_list = []

# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

# Define string with placeholders
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")

# Use format to print strings
for my_string in my_list:
    print(my_string.format(first_pos, second_pos))
