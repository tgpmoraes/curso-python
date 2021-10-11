import pandas as pd
import streaming_ds


non_mus_tcks = pd.DataFrame(streaming_ds.non_mus_tcks,
                            columns=streaming_ds.non_mus_tcks_col)
top_invoices = pd.DataFrame(streaming_ds.top_invoices,
                            columns=streaming_ds.top_invoices_cols)
genres = pd.DataFrame(streaming_ds.genre,
                      columns=streaming_ds.genre_cols)

# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid': 'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))
