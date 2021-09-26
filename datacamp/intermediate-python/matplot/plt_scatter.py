import matplotlib.pyplot as plt
import projection_pop as proj
import numpy as np


gdp_cap = proj.gdp_cap
life_exp = proj.life_exp
pop = proj.pop_country
np_pop = np.array(proj.pop_country)
col = proj.col

# Double np_pop
np_pop = np_pop * 2

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp, s=np_pop, c=col, alpha=0.8)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# After customizing, display the plot
plt.show()
