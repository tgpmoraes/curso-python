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

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'])

# Call the show function
plt.show()
