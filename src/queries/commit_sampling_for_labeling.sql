select
repo_name
, commit
, subject
, message_without_subject
, '' as Is_Summary
, '' as Is_Generic
, '' as Comment
, '' as Certain
, '' as Labler
, 'comsum_random_batch_9_july_2021' as Sampling
from
general.plain_commits_dataset
order by
rand()
limit 5000
;