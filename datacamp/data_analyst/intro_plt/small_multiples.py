import pandas as pd
import matplotlib.pyplot as plt
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_plt'
os.chdir(data_dir)

seattle_weather = pd.read_csv('seattle_weather.csv')
seattle_weather['DATE'] = pd.to_datetime(
    seattle_weather['DATE'],
    format='%m')
seattle_weather['MONTH'] = seattle_weather['DATE'] \
    .dt.strftime('%b')
austin_weather = pd.read_csv('austin_weather.csv')
austin_weather['DATE'] = pd.to_datetime(
    austin_weather['DATE'],
    format='%m')
austin_weather['MONTH'] = austin_weather['DATE'] \
    .dt.strftime('%b')


# Filtering only USW00094290 Station for seattle data
seattle_weather = seattle_weather[
    seattle_weather['STATION'] == 'USW00094290']

# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle
# precipitation
ax[0, 0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1, 0].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1, 1].plot(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'])
plt.show()
