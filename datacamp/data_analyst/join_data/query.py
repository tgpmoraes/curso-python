import pandas as pd
import matplotlib.pyplot as plt
import gdp_pop


gdp = pd.DataFrame(gdp_pop.gdp,
                   columns=gdp_pop.gdp_cols)
pop = pd.DataFrame(gdp_pop.pop,
                   columns=gdp_pop.pop_cols)

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(
    gdp, pop,
    on=['country', 'date'],
    fill_method='ffill'
)

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()
