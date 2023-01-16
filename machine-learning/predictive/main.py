# Importing Libraries

import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report


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

X_train, X_test, y_train, y_test = train_test_split(X, y,train_size=0.8,random_state=1)

#fitting the model with random forest model

model = RandomForestClassifier(n_estimators =100)
model.fit(X_train, y_train)

#prediction and testing

y_pred=model.predict(X_test)

# Report and Accuracy Score

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

print("Classification Report RF:\n",classification_report(y_test,y_pred))




