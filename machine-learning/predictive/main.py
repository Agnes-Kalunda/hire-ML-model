# Importing Libraries

import pandas as pd

import numpy as np

dataset = pd.read_csv('hirable.csv')

# Cleaning up dataset

dataset = dataset.drop([

"sl_no",

"ssc_p",

"ssc_b",

"hsc_p",

"hsc_b",

"hsc_s",

"specialisation",

"salary",

"degree_t"

], axis=1)

dataset = dataset.rename(columns = {'degree_p': 'bsc', 'mba_p': 'msc'})

dataset['gender'] = dataset.gender.replace(['M', 'F'], [1, 2])

dataset['workex'] = dataset.workex.replace(['Yes', 'No'], [1, 0])

dataset['status'] = dataset.status.replace(['Placed', 'Not Placed'], [1, 0])

print (dataset)

# Downscalling Method For BSc & MSc grades

def downscale(score):

    return score/10/2

degrees = ['bsc', 'msc']

for col in degrees:

   dataset[col] = downscale(dataset[col])

# Separating into dependent and independent variables

X = dataset.drop(['status'], axis=1)

y = dataset.status