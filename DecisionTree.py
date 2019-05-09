from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import numpy

def DecisionTreeA(X_train, y_train, X_test, User_Id):
    dt = DecisionTreeClassifier()
    clf = dt.fit(X_train, y_train)
    print('Accuracy of Decision Tree classifier on training set: {:.2f}'
         .format(clf.score(X_train, y_train)))

    pred = dt.predict(X_test)
    pred1 = []
    a = 0
    for i in pred:
        pred1.append([int(User_Id[a]),int(i)])
        a += 1
    
    numpy.savetxt("predictions\\dtpredz.csv", pred1, fmt='%10i',delimiter=",")

    

