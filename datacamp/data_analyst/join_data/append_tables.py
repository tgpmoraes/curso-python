import pandas as pd
import streaming_ds


tracks_ride = pd.DataFrame(streaming_ds.tracks_ride,
                           columns=streaming_ds.tracks_ride_cols)
tracks_master = pd.DataFrame(streaming_ds.tracks_master,
                             columns=streaming_ds.tracks_master_cols)


# Use the .append() method to combine the tracks tables
metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort=False)

# Merge metallica_tracks and invoice_items
tracks_invoices = metallica_tracks.merge(invoice_items, on='tid')

# For each tid and name sum the quantity sold
tracks_sold = tracks_invoices.groupby(['tid','name']).agg({'quantity':'sum'})

# Sort in decending order by quantity and print the results
print(tracks_sold.sort_values('quantity', ascending=False))