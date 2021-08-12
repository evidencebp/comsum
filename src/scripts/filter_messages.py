import os
from os.path import join
import pandas as pd

from configuration import AUX_DATA_PATH, MERGE_COMMIT_FILES, LABELS_PATH, SPLIT_FILE, DATA_PATH, SPLIT_DATA_PATH, \
    SAMPLED_DATA_PATH
from administrative_message_identifier import label_df_as_administrative, ADMINISTRATIVE_COL


def filter_commits(commit_files, filtered_commits_file, split=None):
    print(f"Processing {commit_files}")
    commits_df = pd.read_csv(commit_files)

    # Removing merge commits
    merge_commits_df = pd.read_csv(join(AUX_DATA_PATH
                                        , MERGE_COMMIT_FILES))
    filtered_df = commits_df[~commits_df.commit.isin(merge_commits_df.commit.tolist())]

    # Removing administrative commits
    filtered_df = label_df_as_administrative(filtered_df)
    filtered_df = filtered_df[(filtered_df[ADMINISTRATIVE_COL] == False)]

    if split:
        repos_split_df = pd.read_csv(join(AUX_DATA_PATH, SPLIT_FILE))
        split_repos = repos_split_df[repos_split_df.type == split].repo_name.tolist()
        filtered_df = filtered_df[filtered_df.repo_name.isin(split_repos)]

    print(f"Writing to {filtered_commits_file}, examples:{len(filtered_df)}")
    filtered_df.to_csv(filtered_commits_file, index=False)


if __name__ == "__main__":
    # Usage example, should be applied to each file
    # filter_commits(commit_files=join(LABELS_PATH
    #                                  , 'comsum_random_batch_12_july_2021_labels.csv')
    #                , filtered_commits_file='./tmp/filtered.csv'
    #                , split='Test')

    # # Split all files in SPLIT_DATA_PATH
    # out_dir = SPLIT_DATA_PATH
    # os.makedirs(out_dir, exist_ok=True)
    # for root, dirs, filenames in os.walk(join(DATA_PATH, 'dataset')):
    #     for filename in filenames:
    #         if filename.endswith('zip') or filename.endswith('md'):
    #             continue
    #         if 'train' in filename.lower():
    #             split = 'Train'
    #         else:
    #             split = 'Test'
    #         try:
    #             filter_commits(commit_files=join(root, filename)
    #                            , filtered_commits_file=join(out_dir, filename)
    #                            , split=split)
    #         except Exception as e:
    #             print(f"Failed processing with error type {type(e)} make sure this is a csv like file")

    # Split all files in SAMPLED_DATA_PATH
    out_dir = SPLIT_DATA_PATH
    os.makedirs(out_dir, exist_ok=True)
    for root, dirs, filenames in os.walk(join(SAMPLED_DATA_PATH)):
        for filename in filenames:
            if filename.endswith('zip') or filename.endswith('md'):
                continue
            if 'train' in filename.lower():
                split = 'Train'
            else:
                split = 'Test'
            try:
                filter_commits(commit_files=join(root, filename)
                               , filtered_commits_file=join(out_dir, filename)
                               , split=split)
            except Exception as e:
                print(f"Failed processing with error type {type(e)} make sure this is a csv like file")
