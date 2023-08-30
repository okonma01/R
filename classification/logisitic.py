# logistic regression
from setup import setup_data, path, start_year, end_year
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


# train model from 2012/13 to 2022/23 and store accuracy for each season
accuracy_scores = []

for i in range(start_year, end_year):
    # get data
    X_train, X_test, y_train, y_test = setup_data(path, i)

    # train logistic regression model
    logreg = LogisticRegression(max_iter=1000)
    logreg.fit(X_train, y_train)

    # make predictions
    y_pred = logreg.predict(X_test)

    # evaluate model
    # print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

    accuracy_scores.append(logreg.score(X_test, y_test))

    # classification report
    # print(classification_report(y_test, y_pred))