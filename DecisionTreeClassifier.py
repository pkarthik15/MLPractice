# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:22:58 2019

@author: karthik

Decision Tree Calssifier
 
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_data = pd.read_csv('music.csv');
X = music_data.drop(columns=['genre'])
y = music_data['genre']

X_train, X_test, y_trian, y_test = train_test_split(X, y, test_size=0.2)


model = DecisionTreeClassifier()
model.fit(X_train, y_trian)
predictions = model.predict(X_test)

score = accuracy_score(y_test, predictions)