import pandas as pd
import matplotlib.pyplot as plt
import suspects_lists


gravel = pd.DataFrame(suspects_lists.gravel_list,
                      columns=suspects_lists.gravel_cols)

# Create a histogram of gravel.radius
plt.hist(gravel.radius,
         range=(2, 8),
         bins=40,
         density=True)

# Label plot
plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

# Display histogram
plt.show()
