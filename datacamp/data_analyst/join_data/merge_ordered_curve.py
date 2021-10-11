import matplotlib.pyplot as plt
import pandas as pd
import philips_curve


unemployment = pd.DataFrame(philips_curve.unemployment,
                            columns=philips_curve.unemployment_cols)
inflation = pd.DataFrame(philips_curve.inflation,
                         columns=philips_curve.inflation_cols)


# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(
    inflation,
    unemployment,
    how='inner',
    on='date')

# Print inflation_unemploy
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(x='unemployment_rate', y='cpi', kind='scatter')
plt.show()
