
commit_sampling_for_labeling.sql - sampling random commits for labeling. Has the structure of columns needed for labeling and the sampling batch identifier.

comsum_merge_commits.sql - generates the set of merge commits to allow their removal when needed.

core_terms.sql - generate statistics on predictive power of core terms.

data_set_construction.sql - construct the data set (using the [GeneralGitHub BigQuery infrastrucre](https://github.com/evidencebp/general)).

dataset_properties.sql - descriptive statistics about the data set.

length_distributions.sql - generate length (char/word) distributions

main.sql - instruction for construction

meaning_preserving_samples.sql - sampling from the meaning preserving data set. Note that in this sampling each commit 
should be labeled with respect to the data set concept: corrective, adaptive and refactor.

ps_samples_extraction.sql - build a utility benchmark by pseud-random sampling using the commit hash. This is a reproducible method 
without having to store the sample.

related_commits.sql - builds a data set for the benchmark. Commits and their related ones - commit of the same developer in the same project in a near time.

repo_split.sql - pseudo random train/test/validation split

subject_apperences.sql - generates distributions of common subjects.

subject_in_message.sql - checking for extractive summarization - how often the subject is in the rest of the message.
