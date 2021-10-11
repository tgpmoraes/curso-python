import pandas as pd
import matplotlib.pyplot as plt
import stocks


jpm = pd.DataFrame(stocks.jpm,
                   columns=stocks.jpm_cols)
jpm['date_time'] = pd.to_datetime(
    jpm['date_time'],
    format='%Y-%m-%d %H:%M:%S')
wells = pd.DataFrame(stocks.wells,
                     columns=stocks.wells_cols)
wells['date_time'] = pd.to_datetime(
    wells['date_time'],
    format='%Y-%m-%d %H:%M:%S')
bac = pd.DataFrame(stocks.bac,
                   columns=stocks.bac_cols)
bac['date_time'] = pd.to_datetime(
    bac['date_time'],
    format='%Y-%m-%d %H:%M:%S')

# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(
    jpm, wells, on='date_time',
    suffixes=('', '_wells'),
    direction='nearest')


# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(
    jpm_wells, bac, on='date_time',
    suffixes=('_jpm', '_bac'),
    direction='nearest')


# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()
