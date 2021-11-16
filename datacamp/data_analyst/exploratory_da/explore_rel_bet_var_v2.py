import os
import pandas as pd
import matplotlib.pyplot as plt
from empiricaldist import Pmf


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\exploratory_da\\data'
os.chdir(data_dir)

brfss = pd.read_hdf('brfss.hdf5')

# Extract income
income = brfss['INCOME2']

# Plot the PMF
Pmf.from_seq(income).bar()

# Label the axes
plt.xlabel('Income level')
plt.ylabel('PMF')
plt.show()
