import pandas as pd
import matplotlib.pyplot as plt
import suspects_lists


puppies = pd.DataFrame(suspects_lists.puppies_list,
                       columns=suspects_lists.puppies_cols)

# Create a histogram of the column weight
# from the DataFrame puppies
plt.hist(puppies.weight,
         # bins=50
         range=(5, 35))

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()
