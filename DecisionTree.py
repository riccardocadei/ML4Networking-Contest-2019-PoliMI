from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
import numpy

def DecisionTreeA(X_train, y_train, X_test, User_Id):
    dt = DecisionTreeClassifier(max_depth=9)
    clf = dt.fit(X_train, y_train)
    scores = cross_val_score(dt, X_train, y_train, cv = 10, scoring='precision')
    print(f"Mean crossvalidation Micro-F1: {numpy.mean(scores):.3f}")

    # print('Accuracy of Decision Tree classifier on training set: {:.2f}'.format(clf.score(X_train, y_train)))

    print('ciaone')
     
    pred = dt.predict(X_test)
    pred1 = []
    a = 0
    for i in pred:
        pred1.append([int(User_Id[a]),int(i)])
        a += 1
    
    numpy.savetxt("predictions\\dtpredgs.csv", pred1, fmt='%10i',delimiter=",")

    

