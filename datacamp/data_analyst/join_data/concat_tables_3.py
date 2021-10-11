import pandas as pd
import streaming_ds


classic_18 = pd.DataFrame(streaming_ds.classic_18,
                          columns=streaming_ds.classic_18_cols)
classic_19 = pd.DataFrame(streaming_ds.classic_19,
                          columns=streaming_ds.classic_19_cols)

pop_18 = pd.DataFrame(streaming_ds.pop_18,
                      columns=streaming_ds.pop_18_cols)
pop_19 = pd.DataFrame(streaming_ds.pop_19,
                      columns=streaming_ds.pop_19_cols)

# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)
