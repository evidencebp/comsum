
# Corrective meaning preserving commits
# into mp_not_corrective_commits_labels.csv
select
repo_name
, commit
, message
, '' as Is_Core_Bug
, '' as Is_Corrective
, '' as Justification
, '' as Certain
, '' as Comment
, '12_may_2021_mp_not_corrective_commits' as Sampling
from
general.mp_not_corrective_commits
order by
rand()
limit 500
;

# Refactor meaning preserving commits
# into mp_not_refactor_commits_labels.csv
select
repo_name
, commit
, message
, '' as Is_Core_Refactor
, '' as Is_Refactor
, '' as Justification
, '' as Certain
, '' as Comment
, '12_may_2021_mp_not_refactor_commits' as Sampling
from
general.mp_not_refactor_commits
order by
rand()
limit 500
;

# Adaptive meaning preserving commits
# into mp_not_adaptive_commits_batch_1_labels.csv
select
repo_name
, commit
, message
, '' as Is_Core_Adaptive
, '' as Is_Adaptive
, '' as Justification
, '' as Certain
, '' as Comment
, '12_may_2021_mp_not_adaptive_commits_batch_1' as Sampling
from
general.mp_not_adaptive_commits_batch_1
order by
rand()
limit 500
;
