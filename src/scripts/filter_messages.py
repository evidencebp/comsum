from os.path import join
import pandas as pd

from configuration import AUX_DATA_PATH, MERGE_COMMIT_FILES, LABELS_PATH, SPLIT_FILE
from administrative_message_identifier import label_df_as_administrative, ADMINISTRATIVE_COL

def filter_commits(commit_files
                   , filtered_commits_file
                   , split=None):
    # TODO - add repo filter

    commits_df = pd.read_csv(commit_files)

    # Removing merge commits
    merge_commits_df = pd.read_csv(join(AUX_DATA_PATH
                                  , MERGE_COMMIT_FILES))
    filtered_df = commits_df[~commits_df.commit.isin(merge_commits_df.commit.tolist())]

    # Removing administrative commits
    filtered_df = label_df_as_administrative(filtered_df)
    filtered_df = filtered_df[(filtered_df[ADMINISTRATIVE_COL] == False)]

    if split:
        repos_split_df =  pd.read_csv(join(AUX_DATA_PATH
                                  , SPLIT_FILE))
        split_repos = repos_split_df[repos_split_df.type == split].repo_name.tolist()
        filtered_df = filtered_df[filtered_df.repo_name.isin(split_repos)]

    filtered_df.to_csv(filtered_commits_file
                       , index=False)

if __name__ == "__main__":
    # Usage example, should be applied to each file
    filter_commits(commit_files=join(LABELS_PATH
                        , 'comsum_random_batch_12_july_2021_labels.csv')
                    , filtered_commits_file='/tmp/filtered.csv'
                    , split='Test')