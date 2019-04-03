from sklearn import feature_selection
import pandas as pd

df = pd.read_csv("../dataset/features.csv")

y = df['Label'].values

X = df.loc[:, ~df.columns.isin(['Label', 'Post_ID'])].values

res_sk = feature_selection.mutual_info_classif(X, y)

rdf = pd.DataFrame(list(dict(zip(df.columns[1:-2], res_sk)).items()), columns=['Feature', 'Info_Gain'])\
    .sort_values(by='Info_Gain', ascending=False)

print(rdf)
rdf.to_csv("../dataset/info_gain.csv")
