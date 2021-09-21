# %%
import pandas as pd
import matplotlib.pylab as plt
import numpy as np

file_path = 'Streamlined-Data-Ingestion-with-pandas-Datacamp-main'
data = pd.read_csv(f'../{file_path}/vt_tax_data_2016.csv')

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
# %%
plt.figure()
plt.plot(np.sin(np.linspace(-np.pi, np.pi, 1001)))
plt.show()

# %%
