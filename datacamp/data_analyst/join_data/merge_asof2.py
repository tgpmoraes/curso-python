import pandas as pd
import matplotlib.pyplot as plt
import stocks


gdp = pd.DataFrame(stocks.gdp,
                   columns=stocks.gdp_cols)
gdp['date'] = pd.to_datetime(
    gdp['date'],
    format='%Y-%m-%d %H:%M:%S')
recession = pd.DataFrame(stocks.recession,
                         columns=stocks.recession_cols)
recession['date'] = pd.to_datetime(
    recession['date'],
    format='%Y-%m-%d %H:%M:%S')

# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on='date')

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s == 'recession'
                else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind='bar', y='gdp', x='date', color='green', rot=90)
plt.show()
