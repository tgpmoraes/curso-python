import pokemon_types


names = pokemon_types.names

ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix',
               'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle']

misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon',
                 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']

brock_pokedex = ['Onix', 'Geodude', 'Zubat', 'Golem', 'Vulpix', 'Tauros',
                 'Kabutops', 'Omastar', 'Machop', 'Dugtrio']

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

# Run in interactive window
# %timeit -r5 -n25 'Psyduck' in ash_pokedex
# %timeit -r5 -n25 'Psyduck' in brock_pokedex_set
# %timeit -r5 -n25 'Machop' in ash_pokedex
# %timeit -r5 -n25 'Machop' in brock_pokedex_set


def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques


# Use the provided function to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))
