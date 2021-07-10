# Extracts the data set for commit summarization

drop table if exists general.mp_not_corrective_commits_batch2;

create table
general.mp_not_corrective_commits_batch2
as
select
repo_name
, commit
, general.bq_dataset_type(commit) as dataset_type
, subject
, message
, substr(message, length(subject)+1) as message_without_subject
from
general.enhanced_commits
where
length(message)  > length(subject) # Requiring meaningful summarization
and length(subject) > 0
and
commit_timestamp < '2021-01-01' # Enabling reproducibility in the future
# Semantic condition
and
not is_corrective # not identified as a bug
and general.bq_core_bug(message) > 0 # Functions hash 4b76d8e76af938824f91f4b99247731c21e37ff9
                                     # Note that this function keep improving, hence changing
#and
#substr(commit, 8,1) in ('a','8', '6')
#and
#substr(commit, 5,1) in ('1', '3', '4')
;

# Note two more reproducability issues
# The general.enhanced_commits is create using the general repository
# That depends on the repos table, currenty populated by the 200+ commits during 2019 projects (see CCP paper).
# Other than that the BQ schema keeps updating and projects are also being *REMOVED*.

drop table if exists general.mp_not_refactor_commits_batch2;

create table
general.mp_not_refactor_commits_batch2
as
select
repo_name
, commit
, general.bq_dataset_type(commit) as dataset_type
, subject
, message
, substr(message, length(subject)+1) as message_without_subject
from
general.enhanced_commits
where
length(message)  > length(subject) # Requiring meaningful summarization
and length(subject) > 0
and
commit_timestamp < '2021-01-01' # Enabling reproducibility in the future
# Semantic condition
and
not is_refactor # not identified as a refactor
and general.bq_core_refactor(message) > 0 # Functions hash 4b76d8e76af938824f91f4b99247731c21e37ff9
                                     # Note that this function keep improving, hence changing
#and
#substr(commit, 9,1) in ('a','8', '6')
#and
#substr(commit, 4,1) in ('1', '3', '4')
;



drop table if exists general.mp_not_adaptive_commits_batch2;

create table
general.mp_not_adaptive_commits_batch2
as
select
repo_name
, commit
, general.bq_dataset_type(commit) as dataset_type
, subject
, message
, substr(message, length(subject)+1) as message_without_subject
from
general.enhanced_commits
where
length(message)  > length(subject) # Requiring meaningful summarization
and length(subject) > 0
and
commit_timestamp < '2021-01-01' # Enabling reproducibility in the future
# Semantic condition
and
not is_adaptive # not identified as a adaptive
and general.bq_core_adaptive(message) > 0 # Functions hash 4b76d8e76af938824f91f4b99247731c21e37ff9
                                     # Note that this function keep improving, hence changing
#and
#substr(commit, 7,1) in ('a','8')
#and
#substr(commit, 2,1) in ('1', '3' )
;