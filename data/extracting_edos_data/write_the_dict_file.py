import numpy as np
import pandas as pd
import h5py

filename = 'events_and_ids.csv'

csv_df = pd.read_csv(filename)

to_write_to_dict = ''

for index, row in csv_df.iterrows():
    to_write_to_dict = to_write_to_dict + 'event' + str(index) + " " + str(index) + '\n'

text_file = open("train.dict", 'w')
text_file.write(to_write_to_dict)
text_file.close()