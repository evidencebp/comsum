select
d.repo_name
, d.commit
, d.subject
, d.message_without_subject
, ec.parents > 1 as multiple_parents
, '' as Is_Summary
, '' as Is_Generic
, '' as Category
, '' as Comment
, '' as Certain
, '' as Labler
, 'comsum_random_batch_12_july_2021' as Sampling
from
general.plain_commits_dataset as d
join
general.enhanced_commits as ec
on
d.repo_name = ec.repo_name
and
d.commit = ec.commit
order by
rand()
limit 5000
;