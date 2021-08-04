# data

aux_datasets - more data sets usefull to use the main data set. 
aux_datasets\comsum_merge_commits.csv.zip list the merge commits so they can be removed for suitable use cases.
aux_datasets\repos_split.csv.zip - splits repositories into train/validation/test

images - images showing the use of commit's subject as a summary.

labels - manually labeled commits of random commits (as a summarization) and meaning perserving commits (by their concept).

stats - the results of the related queries.

The commit data itself is hosted [here](https://figshare.com/articles/dataset/CumSum_data_set/14711370)

The files are very large and therefore they are zipped and splited.
Train data is in the files with prefix "plain_commits_dataset_train".
Validation data is in the file "plain_commits_dataset_validation.csv.zip".
Test data is in the file "plain_commits_dataset_test.csv.zip".

The meaning preserving commits are in the following files:
Corrective in "mp_not_corrective_commits.csv.zip", refactor in "mp_not_refactor_commits.csv.zip".
There are many meaning preserving adaptive commits so a sample of them is in "mp_not_adaptive_commits_batch_1.csv.zip"

An example of conversion of the downloaded data into training files (for HuggingFace\pytorch lightning) is found in convert_csv.py
