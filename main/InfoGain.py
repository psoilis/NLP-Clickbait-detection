from sklearn import feature_selection
import pandas as pd


def information_gain(n):
    """
    Function that calculates the information gain of our feature space and selects the top n features

    :arg n: output size after the info gain

    :return: creates the file with the top n features derived from the info gain
    """

    tp = pd.read_csv("dataset/features.csv", iterator=True, chunksize=1000)  # Read the entire dataset
    df = pd.concat(tp, ignore_index=True)  # Trick to read the big csv file

    y = df['Label'].values  # Get the labels

    x = df.loc[:, ~df.columns.isin(['Label', 'Post_ID'])].values  # Get the feature vectors

    col = df.columns  # Get the column names

    del tp, df  # delete the initial dataframe for memory management

    #  Vector specifying if a feature is discrete or continuous
    discrete = [True]*16 + [False]*2 + [True]*3 + [False] + [True]*2 + [False] + [True] + [False]*8 + [True]*3 + \
               [False] + [True]*2 + [False] + [True] + [False]*8 + [True]*(len(col)-52)

    # Run the information gain algorithm
    res_sk = feature_selection.mutual_info_classif(x, y, discrete_features=discrete)

    # Make the info gain output as a dataframe with the correct feature names and info gain values in ascending order
    rdf = pd.DataFrame(list(dict(zip(col[2:-1], res_sk)).items()), columns=['Feature', 'Info_Gain'])\
        .sort_values(by='Info_Gain', ascending=False)

    # Delete the unused objects for memory management
    del col, x, y

    # Write the info gain dataframe to disk
    rdf.to_csv("dataset/info_gain.csv",  index=False)

    # Select the columns to keep with the top n info gain values
    keep = ['Label', 'Post_ID'] + list(rdf['Feature'].values[0:n])

    # Read the original dataset and keep only the selected columns and write the resulting dataset to disk
    tp = pd.read_csv("dataset/features.csv", iterator=True, chunksize=1000)
    df = pd.concat(tp, ignore_index=True)
    df.loc[:, df.columns.isin(keep)].to_csv("dataset/final_feature_vectors_"+n+".csv",  index=False)
