# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ag1g5BCsw6YTpzEWG2ZhETjyathyjE4U
"""

# Importing the required packages
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

# Loding the dataset
data = pd.read_csv("/content/Fish.csv")

data.isnull().sum().sum()

data.head()

# shape of the dataframe
data.shape

# lets print the count of target
data['Species'].value_counts()

# creating instance of labelencoder
labelencoder = LabelEncoder()
# Assigning numerical values and storing in another column
data['Species_values'] = labelencoder.fit_transform(data['Species'])

data.sample(n=10)

# taking all the independent values in x and class value in y
x = data.drop(columns = ['Species','Species_values'],axis = 1)
y = data['Species_values']

# printing x
x.head()



# printing y
y.sample(n= 5)



X_resampled, y_resampled = SMOTE().fit_resample(x, y)
print(sorted(Counter(y_resampled).items()))

"""**Train Test Split**"""

# splitting  the data into train and test in 80:20 ratio
X_train, X_test, Y_train, Y_test = train_test_split(X_resampled,y_resampled, test_size = 0.2, random_state=2)

# shape of training and testing datasets
print(X_train.shape, X_test.shape,Y_train.shape, Y_test.shape)

model= RandomForestClassifier(max_depth = 5,min_samples_leaf=4, random_state=42)

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test) # predicting on testset
train = model.predict(X_train) # predicting on testset

print('Accuracy score of the testing data : ', accuracy_score( Y_train, train))

# Accuracy Score
testing_data_accuracy= accuracy_score( Y_test, Y_pred)
print('Accuracy score of the testing data : ', testing_data_accuracy)

import pickle

# Save the model
pickle.dump(model, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

print(model.predict([[567.0	,43.2,	46.0,	48.7,	7.7920,	4.8700]]))
