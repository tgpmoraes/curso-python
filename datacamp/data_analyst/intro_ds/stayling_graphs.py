import pandas as pd
import matplotlib.pyplot as plt

cols = ['Year', 'Phoenix Police Dept', 'Los Angeles Police Dept',
        'New York City Police Dept', 'Philadelphia Police Dept']
data_list = [[2010.0, 1.08, 0.46, 0.21, 0.71],
             [2011.0, 1.27, 0.45, 0.22, 0.79],
             [2012.0, 1.21, 0.43, 0.22, 0.78],
             [2013.0, 1.11, 0.41, 0.2, 0.67],
             [2014.0, 0.94, 0.39, 0.19, 0.62]]

data = pd.DataFrame(data_list, columns=cols)

# View all styles by typing print(plt.style.available) in the console
# Change the style to ggplot
plt.style.use('bmh')

# Change the color of Phoenix to `"DarkCyan"`
plt.plot(data["Year"], data["Phoenix Police Dept"],
         label="Phoenix", color='DarkCyan')

# Make the Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"],
         label="Los Angeles", linestyle=':')

# Add square markers to Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"],
         label="Philadelphia", marker='s')

# Add a legend
plt.legend()

# Display the plot
plt.show()
