import matplotlib.pyplot as plt
from decision_tree import accuracy_scores as dt_accuracy_scores
from naive_bayes import accuracy_scores as nb_accuracy_scores
from random_forest import accuracy_scores as rf_accuracy_scores
from knn import accuracy_scores as knn_accuracy_scores
from logisitic import accuracy_scores as log_accuracy_scores

# plot accuracy scores of each model on one graph, with each season on the x-axis, and accuracy on the y-axis
plt.plot(range(2012, 2023), dt_accuracy_scores, label='Decision Tree')
plt.plot(range(2012, 2023), nb_accuracy_scores, label='Naive Bayes')
plt.plot(range(2012, 2023), rf_accuracy_scores, label='Random Forest')
plt.plot(range(2012, 2023), knn_accuracy_scores, label='K-Nearest Neighbours')
plt.plot(range(2012, 2023), log_accuracy_scores, label='Logistic Regression')
plt.xlabel('Season')
plt.ylabel('Accuracy')
plt.title('Accuracy of Classification Models')
plt.legend()
plt.show()

