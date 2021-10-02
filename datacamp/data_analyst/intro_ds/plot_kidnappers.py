import pandas as pd
import matplotlib.pyplot as plt
import suspects_lists


ransom = pd.DataFrame(suspects_lists.ransom_list,
                      columns=suspects_lists.ransom_cols)
suspect1 = pd.DataFrame(suspects_lists.suspect1_list,
                        columns=suspects_lists.suspect1_cols)
suspect2 = pd.DataFrame(suspects_lists.suspect2_list,
                        columns=suspects_lists.suspect2_cols)

# x should be ransom.letter and y should be ransom.frequency
plt.plot(ransom.letter, ransom.frequency,
         # Label should be "Ransom"
         label="Ransom",
         # Plot the ransom letter as a dotted gray line
         linestyle=':', color='gray')

# X-values should be suspect1.letter
# Y-values should be suspect1.frequency
# Label should be "Fred Frequentist"
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')

# X-values should be suspect2.letter
# Y-values should be suspect2.frequency
# Label should be "Gertrude Cox"
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend()

# Display plot
plt.show()
