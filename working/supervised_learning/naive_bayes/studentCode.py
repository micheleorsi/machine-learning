from classify import NBAccuracy
from working.supervised_learning.naive_bayes.prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData()

def submitAccuracy():
    accuracy = NBAccuracy(features_train, labels_train, features_test, labels_test)
    return accuracy