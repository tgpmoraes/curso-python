import matplotlib.pyplot as plt
import pandas as pd
import streaming_ds


inv_jul = pd.DataFrame(streaming_ds.inv_jul,
                       columns=streaming_ds.inv_jul_cols)
inv_aug = pd.DataFrame(streaming_ds.inv_aug,
                       columns=streaming_ds.inv_aug_cols)
inv_sep = pd.DataFrame(streaming_ds.inv_sep,
                       columns=streaming_ds.inv_sep_cols)

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep],
                            keys=['7Jul', '8Aug', '9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total': 'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()
