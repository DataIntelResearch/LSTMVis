import numpy as np
import pandas as pd
import h5py

filename = 'LSTM_all_activations.csv'
resultant_filename = 'states.hdf5'

csv_df = pd.read_csv(filename)

# Creates matrices for capturing the state values
layer1_hidden_states_mx = []
layer1_cell_states_mx = []
layer2_hidden_states_mx = []
layer2_cell_states_mx = []

for (columnName, columnData) in csv_df.iteritems():
    if('lstm_1/while/Exit_3' in columnName):
        layer1_hidden_states_mx.append(csv_df[columnName])
    if('lstm_1/while/Exit_4' in columnName):
        layer1_cell_states_mx.append(csv_df[columnName])
    if('lstm_2/while/Exit_3' in columnName):
        layer2_hidden_states_mx.append(csv_df[columnName])
    if('lstm_2/while/Exit_4' in columnName):
        layer2_cell_states_mx.append(csv_df[columnName])


# Creates a dataframe to write the state information to. 
layer1_hidden_states_df = pd.DataFrame(data=layer1_hidden_states_mx)
layer1_cell_states_df = pd.DataFrame(data=layer1_cell_states_mx)
layer2_hidden_states_df = pd.DataFrame(data=layer2_hidden_states_mx)
layer2_cell_states_df = pd.DataFrame(data=layer2_cell_states_mx)

# Create and open the new file to write to.
hdf_df = h5py.File('states.hdf5', 'w')

# Write to that file.
# layer1_hidden_states
hdf_df.create_dataset("states1", data=layer1_hidden_states_df)

# layer1_cell_states
hdf_df.create_dataset("states2", data=layer1_cell_states_df)

# layer2_hidden_states
hdf_df.create_dataset("output1", data=layer2_hidden_states_df)

# layer2_cell_states
hdf_df.create_dataset("output2", data=layer2_cell_states_df)


# Close the new file. 
hdf_df.close()