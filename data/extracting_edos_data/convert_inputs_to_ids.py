import numpy as np
import pandas as pd
import h5py

filename = 'list_of_input_events.csv'

csv_df = pd.read_csv(filename)

current_id = 1

dict_of_events = {}

for index, row in csv_df.iterrows():
    new_event = []
    for i in range(0, 30):
        new_event.append(row[i])

    dict_of_events[str(new_event)] = current_id
    current_id = current_id + 1

list_of_events = []
list_of_ids = []

for k, v in dict_of_events.items():
    list_of_events.append(k)
    list_of_ids.append(v)

final = pd.DataFrame([list_of_events, list_of_ids]).T
final.to_csv('events_and_ids.csv', index=False, header=False)

# THIS IS NOT PROPER AND NEEDS TO BE FIXED
# Create and open the new file to write to.
hdf_df = h5py.File('train.hdf5', 'w')

# Write to that file.
hdf_df.create_dataset("words", data=list_of_ids)

# Close the new file. 
hdf_df.close()