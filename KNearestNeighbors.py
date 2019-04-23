from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report   
import numpy

def KNearestNeighborsA (X_train, y_train, X_test):
    
    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    print('Accuracy of K-NN classifier on training set: {:.2f}'
         .format(knn.score(X_train, y_train)))


    pred = knn.predict(X_test)
    
    pred1 = []
    a = 0
    for i in pred:
        pred1.append([int(X_test.User_Id[a]),int(i)])
        a += 1

    numpy.savetxt("predictions\\knnpred.csv", pred1, fmt='%10i',delimiter=",")