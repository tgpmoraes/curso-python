import pandas as pd
import gdp_pop


gdp = pd.DataFrame(gdp_pop.gdp,
                   columns=gdp_pop.gdp_cols)
pop = pd.DataFrame(gdp_pop.pop,
                   columns=gdp_pop.pop_cols)

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
# ctry_date = pd.merge_ordered(gdp, pop, on=['date', 'country'],
#                              fill_method='ffill')

# Print ctry_date
# print(ctry_date)

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=['country', 'date'],
                             fill_method='ffill')

# Print date_ctry
print(date_ctry)
