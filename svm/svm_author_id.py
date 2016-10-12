#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
import numpy as np
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
features_train = features_train[:len(features_train)]
labels_train = labels_train[:len(labels_train)]
clf = SVC(C=5500.0, kernel='rbf')
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t0 = time()
predict = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

print "Accurancy:", accuracy_score(predict, labels_test)
print "Predicted Answer for 10th email:", predict[10]
print "Predicted Answer for 26th email:", predict[26]
print "Predicted Answer for 50th email:", predict[50]
print "Number of Sara's email:", predict.size - np.sum(predict)
print "Number of Chris's email:", np.sum(predict)

#########################################################
