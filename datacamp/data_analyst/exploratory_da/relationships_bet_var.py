import os
import pandas as pd
import matplotlib.pyplot as plt
from empiricaldist import Pmf


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\exploratory_da\\data'
os.chdir(data_dir)

brfss = pd.read_hdf('brfss.hdf5')

# Extract age
age = brfss['AGE']

# Plot the PMF
pmf_age = Pmf.from_seq(age)
pmf_age.bar()

# Label the axes
plt.xlabel('Age in years')
plt.ylabel('PMF')
plt.show()
