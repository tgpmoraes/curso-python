import pandas as pd
import matplotlib.pyplot as plt

hours_columns = ['officer', 'avg_hours_worked', 'std_hours_worked',
                 'desk_work', 'field_work']
hours_list = [['Deshaun', 45, 3, 25, 20], ['Mengfei', 33, 9, 20, 13],
              ['Aditya', 42, 5, 12, 30]]
hours = pd.DataFrame(hours_list, columns=hours_columns)

# Display the DataFrame hours using print
print(hours)

# Create a bar plot from the DataFrame hours
# plt.bar(hours.officer, hours.avg_hours_worked,
#         # Add error bars
#         yerr=hours.std_hours_worked)

# Plot the number of hours spent on desk work
plt.bar(hours.officer, hours.desk_work,
        label='Desk Work')

# Plot the hours spent on field work on top of desk work
plt.bar(hours.officer, hours.field_work,
        bottom=hours.desk_work,
        label='Field Work')

# Add a legend
plt.legend()

# Display the plot
plt.show()
