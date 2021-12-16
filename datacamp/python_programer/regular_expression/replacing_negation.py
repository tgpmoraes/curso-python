movies = ("the rest of the story isn't important because all it does is serve "
          "as a mere backdrop for the two stars to share the screen .")

# Replace negations
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)
