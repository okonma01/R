import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn import preprocessing
import matplotlib.pyplot as plt
import mplcursors
import sys

df = pd.DataFrame(pd.read_csv('../data/shooting-2012-2023.csv'))

# set default args for 2023 season
if len(sys.argv) == 1:
    sys.argv.append('2023')
elif sys.argv[1].isdigit() == False:
    sys.argv[1] = '2023'

df_clean = df.dropna()

# remove first two columns - df.iloc[:, 2:]

# drop columns
# df_clean = df_clean.drop(columns=['fg_per_36_min', 'fga_per_36_min', 'fg_percent', 'percent_fga_from_x2p_range', 'fg_percent_from_x2p_range', 'fg_percent_from_x3p_range', 'corner_3_point_percent'])


# filter by season
df_clean = df_clean.loc[df_clean['season'] == int(sys.argv[1])]
df_clean = df_clean[['player', 'pos', 'percent_fga_from_x0_3_range', 'percent_fga_from_x3_10_range', 'percent_fga_from_x10_16_range', 'percent_fga_from_x16_3p_range', 'percent_fga_from_x3p_range']]

# select only pg and sg
df_clean = df_clean.loc[df_clean['pos'].isin(['SF', 'PF'])]

scaled_data = preprocessing.scale(df_clean.iloc[:, 2:])

lda = LDA(n_components=2)
lda.fit(scaled_data, df_clean['pos'])
lda_data = lda.transform(scaled_data)

# plot data
per_var = np.round(lda.explained_variance_ratio_ * 100, decimals=1)
labels = ['LD' + str(i) for i in range(1, len(per_var) + 1)]

plt.bar(x=range(1, len(per_var) + 1), height=per_var, tick_label=labels)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Linear Discriminant')
plt.title('Scree Plot')
plt.show()

lda_df = pd.DataFrame(lda_data, columns=labels)

plt.scatter(lda_df.LD1, lda_df.LD2)
plt.title('My LDA Graph')
plt.xlabel('LD1 - {0}%'.format(per_var[0]))
plt.ylabel('LD2 - {0}%'.format(per_var[1]))

cursor = mplcursors.cursor(hover=True)  # Create a cursor object

def on_hover(sel):
    sample = sel.index
    player_name = df_clean.iloc[sample]['player']
    player_name += '\n' + '0 - 3ft: ' + round(df_clean.iloc[sample]['percent_fga_from_x0_3_range'] * 100, 2).astype(str) + '%'
    player_name += '\n' + '3 - 10ft: ' + round(df_clean.iloc[sample]['percent_fga_from_x3_10_range'] * 100, 2).astype(str) + '%'
    player_name += '\n' + '10 - 16ft: ' + round(df_clean.iloc[sample]['percent_fga_from_x10_16_range'] * 100, 2).astype(str) + '%'
    player_name += '\n' + '16 - 3pt: ' + round(df_clean.iloc[sample]['percent_fga_from_x16_3p_range'] * 100, 2).astype(str) + '%'
    player_name += '\n' + '3pt: ' + round(df_clean.iloc[sample]['percent_fga_from_x3p_range'] * 100, 2).astype(str) + '%'
    sel.annotation.set_text(player_name)  # Set the label text

cursor.connect("add", on_hover)  # Connect the cursor event to the on_hover function

plt.show()

