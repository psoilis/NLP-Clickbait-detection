from sklearn import feature_selection
import pandas as pd

df = pd.read_csv("../dataset/features_large.csv")

y = df['Label'].values

X = df.loc[:, ~df.columns.isin(['Label', 'Post_ID'])].values

discrete = [True]*11 + [False] + [True]*3 + [False] + [True]*2 + [False] + [True] + [False]*8 + [True]*3 + [False] + \
           [True]*2 + [False] + [True] + [False]*8 + [True]*(len(df.columns)-46)

res_sk = feature_selection.mutual_info_classif(X, y, discrete_features=discrete)

rdf = pd.DataFrame(list(dict(zip(df.columns[2:-1], res_sk)).items()), columns=['Feature', 'Info_Gain'])\
    .sort_values(by='Info_Gain', ascending=False)

rdf.to_csv("../dataset/info_gain.csv")
########################################################################################################################
"""""""""
Xngrams = df.iloc[:, 74:-1]
dngrams = [True]*len(Xngrams.columns)

res_ng = feature_selection.mutual_info_classif(Xngrams.values, y, discrete_features=dngrams )

rdf_ng = pd.DataFrame(list(dict(zip(Xngrams.columns, res_ng)).items()), columns=['Feature', 'Info_Gain'])\
    .sort_values(by='Info_Gain', ascending=False)


top_ngrams = 40

non_top_ngrams = list(rdf_ng['Feature'].values[top_ngrams-1:-1])

df_top_ngrams = df.loc[:, ~df.columns.isin(non_top_ngrams)]

y = df_top_ngrams['Label'].values

X = df_top_ngrams.loc[:, ~df_top_ngrams.columns.isin(['Label', 'Post_ID'])].values

discrete = [True]*11 + [False] + [True]*3 + [False] + [True]*2 + [False] + [True] + [False]*8 + [True]*3 + [False] + \
           [True]*2 + [False] + [True] + [False]*8 + [True]*(len(df_top_ngrams.columns)-46)

res_sk = feature_selection.mutual_info_classif(X, y, discrete_features=discrete)

rdf = pd.DataFrame(list(dict(zip(df_top_ngrams.columns[2:-1], res_sk)).items()), columns=['Feature', 'Info_Gain'])\
    .sort_values(by='Info_Gain', ascending=False)

rdf.to_csv("../dataset/info_gain_top_ngrams.csv")
# print(rdf_ng)
#rdf_ng.to_csv("../dataset/info_gain_ngram.csv")
"""""""""
"""""""""
########################################################################################################################

Xwongrams = df.iloc[:, 2:73]
dwongrams = [True]*11 + [False] + [True]*10 + [False]*6 + [True]*10 + [False]*6 + [True]*(len(Xwongrams.columns)-44)

res_wong = feature_selection.mutual_info_classif(Xwongrams.values, y, discrete_features=dwongrams)

rdf_wong = pd.DataFrame(list(dict(zip(Xwongrams.columns, res_wong)).items()), columns=['Feature', 'Info_Gain'])\
    .sort_values(by='Info_Gain', ascending=False)

# print(rdf_wong)
rdf_wong.to_csv("../dataset/info_gain_without_ngram.csv")
########################################################################################################################


n = 10

keep = ['Label', 'Post_ID'] + list(rdf['Feature'].values[0:n-1])

selected_features = df.loc[:, df.columns.isin(keep)]

selected_features.to_csv("../dataset/final_selected_features.csv")
"""""""""