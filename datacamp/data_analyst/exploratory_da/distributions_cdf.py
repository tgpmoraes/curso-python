import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from empiricaldist import Cdf
from scipy.stats import norm


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\exploratory_da\\data'
os.chdir(data_dir)

gss = pd.read_hdf('gss.hdf5')

# For this code to run, it is needed the following library
# https://pypi.org/project/empiricaldist/

# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = Cdf.from_seq(age)

# What fraction of the respondents in the GSS dataset are UNTIL than 30?
# Calculate the CDF of 30
print(cdf_age(30))

cdf_income = Cdf.from_seq(gss['realinc'])

# Calculate the 75th percentile
percentile_75th = cdf_income.inverse(0.75)

# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)

# Calculate the interquartile range
iqr = percentile_75th - percentile_25th

# What is the interquartile range (IQR) of income in the GSS datset?
print(iqr)

# Plot it
cdf_income.plot()

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
# plt.show()

# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = (educ >= 14) & ~(bach)

# High school (12 or fewer years of education)
high = (educ <= 12)
print(high.mean())

income = gss['realinc']

# Plot the CDFs
Cdf.from_seq(income[high]).plot(label='High school')
Cdf.from_seq(income[assc]).plot(label='Associate')
Cdf.from_seq(income[bach]).plot(label='Bachelor')

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
# plt.show()

# Extract realinc and compute its log
income = gss['realinc']
log_income = np.log10(income)

# Compute mean and standard deviation
mean = log_income.mean()
std = log_income.std()
print(mean, std)

# Make a norm object
dist = norm(mean, std).cdf(income)
