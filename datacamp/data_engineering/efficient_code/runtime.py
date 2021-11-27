# %%
import numpy as np
# Create a list of integers (0-50) using list comprehension
%timeit -r2 -n10 nums_list_comp = [num for num in range(51)]
# print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
%timeit -r2 -n10 nums_unpack = [*range(51)]
# print(nums_unpack)
# %%
import heroes

%timeit -r5 -n25 set(heroes.list_of_heroes)
# %%
# Create a list using the formal name
%timeit -r5 -n25 formal_list = list()
# print(formal_list)

# Create a list using the literal syntax
%timeit -r5 -n25 literal_list = []
# print(literal_list)

# Print out the type of formal_list
# print(type(formal_list))

# Print out the type of literal_list
# print(type(literal_list))
# %%timeit -r5 -n25
hero_wts_lbs = []
for wt in heroes.list_of_wts:
    hero_wts_lbs.append(wt * 2.20462)

# wts_np = np.array(heroes.list_of_wts)
# hero_wts_lbs_np = wts_np * 2.20462

# %%
