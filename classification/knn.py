# k-nearest neighbours
from setup import setup_data, path, start_year, end_year
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

# train model from 2012-13 to 2022-23 and store accuracy for each season
accuracy_scores = []

for i in range(start_year, end_year):
    # get data
    X_train, X_test, y_train, y_test = setup_data(path, i)

    # train k-nearest neighbours model
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    # make predictions
    y_pred = knn.predict(X_test)

    # evaluate model
    # print('Accuracy of k-nearest neighbours classifier on test set: {:.2f}'.format(knn.score(X_test, y_test)))

    accuracy_scores.append(knn.score(X_test, y_test))

    # classification report
    # print(classification_report(y_test, y_pred))