# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:47:59 2019

@author: karthik

Model Visualization of Decision Tree Classifier

"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

music_data = pd.read_csv('music.csv');
X = music_data.drop(columns=['genre'])
y = music_data['genre']


model = DecisionTreeClassifier()
model.fit(X, y)

tree.export_graphviz(model,
                     out_file = 'music-recommender.dot',
                     feature_names = ['age', 'gender'],
                     class_names = sorted(y.unique()),
                     label = 'all',
                     rounded = True,
                     filled = True)

