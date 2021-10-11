import pandas as pd
import streaming_ds


tracks_master = pd.DataFrame(streaming_ds.tracks_master,
                             columns=streaming_ds.tracks_master_cols)
tracks_ride = pd.DataFrame(streaming_ds.tracks_ride,
                           columns=streaming_ds.tracks_ride_cols)
tracks_st = pd.DataFrame(streaming_ds.tracks_st,
                         columns=streaming_ds.tracks_st_cols)

# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)
