import pandas as pd
import matplotlib.pyplot as plt
import os
import plot_ts


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_plt'
os.chdir(data_dir)

climate_change = pd.read_csv(
    'climate_change.csv',
    parse_dates=True,
    index_col='date')

# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_ts.plot_timeseries(
    ax,
    climate_change.index,
    climate_change['co2'],
    "blue",
    'Time (years)',
    'CO2 levels')

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_ts.plot_timeseries(
    ax2,
    climate_change.index,
    climate_change['relative_temp'],
    "red",
    'Time (years)',
    'Relative temperature (Celsius)')

plt.show()
