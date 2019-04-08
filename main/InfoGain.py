from sklearn import feature_selection
import pandas as pd


def information_gain(n):

    tp = pd.read_csv("dataset/features.csv", iterator=True, chunksize=1000)
    df = pd.concat(tp, ignore_index=True)

    y = df['Label'].values

    x = df.loc[:, ~df.columns.isin(['Label', 'Post_ID'])].values

    col = df.columns

    del tp, df

    discrete = [True]*16 + [False]*2 + [True]*3 + [False] + [True]*2 + [False] + [True] + [False]*8 + [True]*3 + \
               [False] + [True]*2 + [False] + [True] + [False]*8 + [True]*(len(col)-52)

    res_sk = feature_selection.mutual_info_classif(x, y, discrete_features=discrete)

    rdf = pd.DataFrame(list(dict(zip(col[2:-1], res_sk)).items()), columns=['Feature', 'Info_Gain'])\
        .sort_values(by='Info_Gain', ascending=False)

    del col, x, y

    rdf.to_csv("dataset/info_gain.csv",  index=False)

    keep = ['Label', 'Post_ID'] + list(rdf['Feature'].values[0:n])

    tp = pd.read_csv("dataset/features.csv", iterator=True, chunksize=1000)
    df = pd.concat(tp, ignore_index=True)

    df.loc[:, df.columns.isin(keep)].to_csv("dataset/final_feature_vectors_80.csv",  index=False)


information_gain(80)
