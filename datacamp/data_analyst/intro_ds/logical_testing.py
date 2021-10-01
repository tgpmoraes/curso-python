import pandas as pd

mpr_list = [['Bayes', 'DataCamp', 'Golden Retriever', 'Still Missing', 1],
            ['Sigmoid', '', 'Dachshund', 'Still Missing', 2],
            ['Sparky', 'Dr. Apache', 'Border Collie', 'Found', 3],
            ['Theorem', 'Joseph-Louis Lagrange', 'French Bulldog', 'Found', 4],
            ['Ned', 'Tim Oliphant', 'Shih Tzu', 'Still Missing', 2],
            ['Benny', 'Hillary Green-Lerman', 'Poodle', 'Found', 3]]

cols = ['Dog Name', 'Owner Name', 'Dog Breed', 'Status', 'Age']

mpr = pd.DataFrame(mpr_list, columns=cols)

# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr['Status'] == 'Still Missing']
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr['Dog Breed'] != 'Poodle']
print(not_poodle)
