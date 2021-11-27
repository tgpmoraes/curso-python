# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import projection_pop as proj


year = proj.year
pop = proj.pop

# Add more data
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0, 2, 4, 6, 8, 10],
           ['0', '2B', '4B', '6B', '8B', '10B'])
# Display the plot with plt.show()
plt.show()
