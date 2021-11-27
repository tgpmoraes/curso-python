import pokemon_types
from collections import Counter
from itertools import combinations
import numpy as np


names = pokemon_types.names
primary_types = pokemon_types.primary_types
generations = pokemon_types.generations
hps_list = pokemon_types.hps

# Collect the count of each generation
gen_counts = Counter(generations)

# for gen,count in gen_counts.items():
#     total_count = len(generations)
#     gen_percent = round(count / total_count * 100, 2)
#     print(
#       'generation {}: count = {:3} percentage = {}'
#       .format(gen, count, gen_percent)
#     )

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen, count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))

# Collect all possible pairs using combinations()
possible_pairs = [*combinations(primary_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

# for i,pair in enumerate(possible_pairs, 1):
#     enumerated_pair_tuple = (i,) + pair
#     enumerated_pair_list = list(enumerated_pair_tuple)
#     enumerated_pairs.append(enumerated_pair_list)

# Append each enumerated_pair_tuple to the empty list above
for i, pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
# print(enumerated_pairs)

hps = np.array(hps_list)
# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# poke_zscores = []

# for name, hp in zip(names, hps):
#     hp_avg = hps.mean()
#     hp_std = hps.std()
#     z_score = (hp - hp_avg)/hp_std
#     poke_zscores.append((name, hp, z_score))

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# highest_hp_pokemon = []

# for name, hp, zscore in poke_zscores:
#     if zscore > 2:
#         highest_hp_pokemon.append((name, hp, zscore))

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')
