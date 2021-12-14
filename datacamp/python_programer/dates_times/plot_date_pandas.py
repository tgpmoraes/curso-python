import matplotlib.pyplot as plt
import os
import pandas as pd


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\dates_times'
os.chdir(data_dir)

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv',
                    parse_dates=['Start date', 'End date'])

# Import matplotlib

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on='Start date')\
    .size()\
    .plot(ylim=[0, 150])

# Show the results
plt.show()
