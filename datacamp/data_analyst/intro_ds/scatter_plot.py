import pandas as pd
import matplotlib.pyplot as plt
import suspects_lists


cellphone = pd.DataFrame(suspects_lists.cellphone_list,
                         columns=suspects_lists.cellphone_cols)

# Explore the data
print(cellphone.head())

# Create a scatter plot of the data from the DataFrame cellphone
plt.scatter(cellphone.x, cellphone.y,
            color='red',
            marker='s',
            alpha=0.1)

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()
