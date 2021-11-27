# %%
import numpy as np

heroes = ['Batman', 'Superman', 'Wonder Woman']
hts = np.array([188.0, 191.0, 183.0])
wts = np.array([95.0, 101.0,  74.0])


def convert_units(heroes, heights, weights):
    new_hts = [ht * 0.39370 for ht in heights]
    new_wts = [wt * 2.20462 for wt in weights]

    hero_data = {}

    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data


%load_ext line_profiler
%lprun - f convert_units convert_units(heroes, hts, wts)
