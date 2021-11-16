import os
import pandas as pd
import matplotlib.pyplot as plt
from empiricaldist import Pmf


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\exploratory_da\\data'
os.chdir(data_dir)

gss = pd.read_hdf('gss.hdf5')

# For this code to run, it is needed the following library
# https://pypi.org/project/empiricaldist/

# Compute the PMF for year
pmf_year = Pmf.from_seq(gss.year, normalize=False)

# Print the result
# print(pmf_year)

# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf.from_seq(age)

# Plot the PMF
pmf_age.bar()

# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()
