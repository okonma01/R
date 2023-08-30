from sklearn.manifold import MDS
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import sklearn.datasets as ds
import seaborn as sns
import sklearn.metrics.pairwise as pw
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

X = np.array([[0, 0, 0], [0, 0, 1], [1, 1, 1], [0, 1, 0], [0, 1, 1]])
mds = MDS(random_state=0)

dist_manhattan = pw.manhattan_distances(X)
X_transform = mds.fit_transform(X)
X_transform_L1 = mds.fit_transform(dist_manhattan)


# Plotting
colors = ['red', 'green', 'blue', 'cyan', 'magenta']
size = [64, 64, 64, 64, 64]
fig = plt.figure(2, (10, 4))
ax = fig.add_subplot(121, projection='3d')
plt.scatter(X[:, 0], X[:, 1], zs=X[:, 2], c=colors, s=size)
plt.title('Original points')

ax = fig.add_subplot(122)
plt.scatter(X_transform[:, 0], X_transform[:, 1], c=colors, s=size)
plt.title('Embedding with Euclidean distance in 2D')
fig.subplots_adjust(wspace=0.4, hspace=0.5)
plt.show()