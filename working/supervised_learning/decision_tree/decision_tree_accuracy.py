import sys
from sklearn import tree
from sklearn.metrics import accuracy_score

from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



########################## DECISION TREE #################################


### your code goes here--now create 2 decision tree classifiers,
### one with min_samples_split=2 and one with min_samples_split=50
### compute the accuracies on the testing data and store
### the accuracy numbers to acc_min_samples_split_2 and
### acc_min_samples_split_50, respectively

clf_2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf_2 = clf_2.fit(features_train, labels_train)

y_pred = []
for val in features_test:
    predicted = clf_2.predict([val])
    y_pred.append(predicted)

acc_min_samples_split_2 = accuracy_score(labels_test, y_pred)

clf_50 = tree.DecisionTreeClassifier(min_samples_split=50)
clf_50 = clf_50.fit(features_train, labels_train)

y_pred = []
for val in features_test:
     predicted = clf_50.predict([val])
     y_pred.append(predicted)

acc_min_samples_split_50 = accuracy_score(labels_test, y_pred)

def submitAccuracies():
  return {"acc_min_samples_split_2":round(acc_min_samples_split_2,3)
  ,"acc_min_samples_split_50":round(acc_min_samples_split_50,3)
  }
