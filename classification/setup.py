import pandas as pd
from sklearn.model_selection import train_test_split    
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import sys

path = '../data/shooting-2012-2023.csv'
start_year = 2012
end_year = 2023

def setup_data(path, i=0):
    # load data into a pandas dataframe
    df = pd.DataFrame(pd.read_csv(path))
    df['pos'] = df['pos'].apply(lambda x: x.split('-')[0])


    # set default args for 2023 season
    if len(sys.argv) == 1 or i == 0:
        sys.argv.append(2023)
    else:
        sys.argv.append(i)

    # drop missing values
    df_clean = df.dropna()

    # filter by season
    df_clean = df_clean.loc[df_clean['season'] == int(sys.argv[1])]

    # define features and target
    features = df_clean.drop(columns=['season', 'player', 'pos'])
    target = df_clean['pos']

    # split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=1)

    # standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test