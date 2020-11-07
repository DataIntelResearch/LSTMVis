import numpy as np
import pandas as pd
import h5py

filename = 'LSTM_all_activations.csv'
resultant_filename = 'states.hdf5'

csv_df = pd.read_csv(filename)
list_of_events = []

for index, row in csv_df.iterrows():
    new_event = []
    for i in range(0, 30):
        new_event.append(row[i])

    list_of_events.append(new_event)

finalized_dataframe = pd.DataFrame(list_of_events)
finalized_dataframe.to_csv('list_of_input_events.csv', index=False, header=False)