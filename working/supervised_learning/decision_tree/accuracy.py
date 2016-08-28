import sys
from sklearn import tree

from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)

y_pred = []
for val in features_test:
    predicted = clf.predict([val])
    y_pred.append(predicted)

#### your code goes here


acc = accuracy_score(labels_test, y_pred)
### be sure to compute the accuracy on the test set



def submitAccuracies():
    return {"acc":round(acc,3)}

