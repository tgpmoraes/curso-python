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

# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
ax[0].plot(
    seattle_weather['MONTH'],
    seattle_weather['MLY-PRCP-NORMAL'],
    color='b')
ax[0].plot(
    seattle_weather['MONTH'],
    seattle_weather['MLY-PRCP-25PCTL'],
    color='b',
    linestyle='--')
ax[0].plot(
    seattle_weather['MONTH'],
    seattle_weather['MLY-PRCP-75PCTL'],
    color='b',
    linestyle='--')

# Plot Austin precipitation data in the bottom axes
ax[1].plot(
    austin_weather['MONTH'],
    austin_weather['MLY-PRCP-NORMAL'],
    color='r')
ax[1].plot(
    austin_weather['MONTH'],
    austin_weather['MLY-PRCP-25PCTL'],
    color='r',
    linestyle='--')
ax[1].plot(
    austin_weather['MONTH'],
    austin_weather['MLY-PRCP-75PCTL'],
    color='r',
    linestyle='--')

plt.show()
