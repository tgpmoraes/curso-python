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

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Plot Seattle data, setting data appearance
ax.plot(
    seattle_weather["MONTH"],
    seattle_weather["MLY-PRCP-NORMAL"],
    color='b',
    marker='o',
    linestyle='--')

# Plot Austin data, setting data appearance
ax.plot(
    austin_weather["MONTH"],
    austin_weather["MLY-PRCP-NORMAL"],
    color='r',
    marker='v',
    linestyle='--')

# Customize the x-axis label
ax.set_xlabel('Time (months)')

# Customize the y-axis label
ax.set_ylabel('Precipitation (inches)')

# Add the title
ax.set_title('Weather patterns in Austin and Seattle')

# Display the figure
plt.show()
