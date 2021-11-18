import os
import pandas as pd
import matplotlib.pyplot as plt

curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\policy_analyze'
os.chdir(data_dir)

# Read 'police.csv' into a DataFrame named ri
ri = pd.read_feather('police.ftr')

# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Calculate the annual rate of drug-related stops
print(ri.drugs_related_stop.resample('A').mean())

# Save the annual rate of drug-related stops
annual_drug_rate = ri.drugs_related_stop.resample('A').mean()

# Create a line plot of 'annual_drug_rate'
# annual_drug_rate.plot()

# Display the plot
# plt.show()

# Calculate and save the annual search rate
annual_search_rate = ri.search_conducted.resample('A').mean()

# Concatenate 'annual_drug_rate' and 'annual_search_rate'
annual = pd.concat([annual_drug_rate, annual_search_rate], axis='columns')

# Create subplots from 'annual'
annual.plot(subplots=True)

# Display the subplots
plt.show()
