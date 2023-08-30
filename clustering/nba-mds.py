import pandas as pd
import numpy as np
from sklearn.manifold import MDS
import sklearn.datasets as ds
from sklearn import preprocessing
import matplotlib.pyplot as plt
import mplcursors
import sys
from sklearn.metrics.pairwise import euclidean_distances, manhattan_distances


df = pd.DataFrame(pd.read_csv('../data/shooting-2012-2023.csv'))

# set default args for 2023 season
if len(sys.argv) == 1:
    sys.argv.append('2023')
elif sys.argv[1].isdigit() == False:
    sys.argv[1] = '2023'

df_clean = df.dropna()

# filter by season
df_clean = df_clean.loc[df_clean['season'] == int(sys.argv[1])]
df_clean = df_clean[['player', 'pos', 'percent_fga_from_x0_3_range', 'percent_fga_from_x3_10_range', 'percent_fga_from_x10_16_range', 'percent_fga_from_x16_3p_range', 'percent_fga_from_x3p_range']]

# select only pg and sg
df_clean = df_clean.loc[df_clean['pos'].isin(['PG', 'SG'])]

scaled_data = preprocessing.scale(df_clean.iloc[:, 2:])

# MDS
mds = MDS(random_state=0)

dist_euclidean = euclidean_distances(scaled_data)
dist_manhattan = manhattan_distances(scaled_data)

X_transform = mds.fit_transform(scaled_data)
X_transform_L1 = mds.fit_transform(dist_manhattan)

# Plot MDS with euclidean distance
fig = plt.figure(1, (10, 4))
ax = fig.add_subplot(121)
plt.scatter(X_transform[:, 0], X_transform[:, 1])
plt.title('Embedding with Euclidean distance in 2D')


def on_hover(sel):
    sample = sel.index
    player_name = df_clean.iloc[sample]['player']
    player_name += '\n' + '0 - 3ft: ' + round(df_clean.iloc[sample]['percent_fga_from_x0_3_range'] * 100, 2).astype(str) + '%'
    player_name += '\n' + '3 - 10ft: ' + round(df_clean.iloc[sample]['percent_fga_from_x3_10_range'] * 100, 2).astype(str) + '%'
    player_name += '\n' + '10 - 16ft: ' + round(df_clean.iloc[sample]['percent_fga_from_x10_16_range'] * 100, 2).astype(str) + '%'
    player_name += '\n' + '16 - 3pt: ' + round(df_clean.iloc[sample]['percent_fga_from_x16_3p_range'] * 100, 2).astype(str) + '%'
    player_name += '\n' + '3pt: ' + round(df_clean.iloc[sample]['percent_fga_from_x3p_range'] * 100, 2).astype(str) + '%'
    sel.annotation.set_text(player_name)  # Set the label text


# Plot MDS with manhattan distance
ax = fig.add_subplot(122)
plt.scatter(X_transform_L1[:, 0], X_transform_L1[:, 1])
plt.title('Embedding with Manhattan distance in 2D')

cursor = mplcursors.cursor(hover=True)  # Create a cursor object
cursor.connect("add", on_hover)  # Connect the cursor event to the on_hover function

plt.show()