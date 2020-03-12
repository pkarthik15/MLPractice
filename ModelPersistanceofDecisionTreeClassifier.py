# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:36:56 2019

@author: karthik

Model Persistance of Decision Tree Classifier

"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

#music_data = pd.read_csv('music.csv');
#X = music_data.drop(columns=['genre'])
#y = music_data['genre']
#
#
#model = DecisionTreeClassifier()
#model.fit(X, y)

#joblib.dump(model, 'music-recommender.joblib')


#model = joblib.load('music-recommender.joblib')
#predictions = model.predict([[21, 1]])
