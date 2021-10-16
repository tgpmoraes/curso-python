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

seattle_weather = seattle_weather[
    seattle_weather['STATION'] == 'USW00094290']

fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(
    seattle_weather['MONTH'],
    seattle_weather['MLY-TAVG-NORMAL'],
    yerr=seattle_weather['MLY-TAVG-STDDEV'])

# Add Austin temperature data in each month with error bars
ax.errorbar(
    austin_weather['MONTH'],
    austin_weather['MLY-TAVG-NORMAL'],
    yerr=austin_weather['MLY-TAVG-STDDEV'])

# Set the y-axis label
ax.set_ylabel('Temperature (Fahrenheit)')

plt.show()
