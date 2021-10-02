import pandas as pd
import matplotlib.pyplot as plt


cols = ['day_of_week', 'hours_worked']
deshaun_list = [['M', 8], ['Tu', 5], ['W', 3], ['Th', 5], ['F', 8]]
aditya_list = [['M', 10], ['Tu', 2], ['W', 1], ['Th', 0], ['F', 0]]
mengfei_list = [['M', 0], ['Tu', 0], ['W', 5], ['Th', 9], ['F', 5]]

deshaun = pd.DataFrame(deshaun_list, columns=cols)
aditya = pd.DataFrame(aditya_list, columns=cols)
mengfei = pd.DataFrame(mengfei_list, columns=cols)

# Officer Deshaun
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')

# Add a label to Aditya's plot
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')

# Add a label to Mengfei's plot
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title("Officer Deshaun's plot of hours worked")

# Add y-axis label
plt.ylabel('Hours worked')

# Add annotation "Missing Thursday and Friday from Mengfei" at (2.5, 80)
plt.text(3, 1, 'Missing Thursday\nand Friday from\nAditya')

# Legend
plt.legend()
# Display plot
plt.show()
