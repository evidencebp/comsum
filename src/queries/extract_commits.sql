# Extracts the data set for commit summarization

CREATE OR REPLACE FUNCTION
general.bq_dataset_type
 (commit string)
 RETURNS string
AS (
    case
        when substr(commit, 1,1) = '0'  then 'Validation'
        when substr(commit, 1,1) = '1'  then 'Test'
        else 'Train' end # Train

 )
;


WITH tab AS (
  SELECT  'c6da5fb38e72a4dc999642e7083c2e26414cb8b1' AS commit
            , 'Train' as expected
    UNION ALL SELECT '06da5fb38e72a4dc999642e7083c2e26414cb8b1'
                    , 'Validation'

    UNION ALL SELECT '16da5fb38e72a4dc999642e7083c2e26414cb8b1'
                    , 'Test'

    UNION ALL SELECT null
                    , null
)
SELECT commit
, expected
, general.bq_dataset_type(commit) as actual
, general.bq_dataset_type(commit) = expected as pass
FROM tab as testing
;



CREATE OR REPLACE FUNCTION
general.bq_dataset_batch
 (commit string)
 RETURNS string
AS (
    case
        when substr(commit, 6,1) in ('2', '4','6', '8', 'a', 'c', 'e')
        and
        substr(commit, 3,1) in ('1', '3', '5', '7', '9', 'b', 'd', 'f')
                then '1'
        when substr(commit, 7,1) in ('2', '4',  '6', '8', 'a', 'c')
            then '2'
        else '3' end # else

 )
;


WITH tab AS (
  SELECT  'c6d11222272a4dc999642e7083c2e26414cb8b1' AS commit
            , '1' as expected
    UNION ALL SELECT '06da5f22272a4dc999642e7083c2e26414cb8b1'
                    , '2'

    UNION ALL SELECT '16da5fb38e72a4dc999642e7083c2e26414cb8b1'
                    , '-1'

    UNION ALL SELECT null
                    , null
)
SELECT commit
, expected
, general.bq_dataset_batch(commit) as actual
, general.bq_dataset_batch(commit) = expected as pass
FROM tab as testing
;


# 8942803
select
count(*)
from
general.enhanced_commits
where
length(message) - 100 > length(subject)
and length(subject) > 0
and
commit_timestamp < '2021-01-01' # Enabling reproducibility in the future
;

drop table if exists general.plain_commits_dataset;

create table
general.plain_commits_dataset
as
select
commit
, max(repo_name) as repo_name
, max(general.bq_dataset_type(commit)) as dataset_type
, max(subject) as subject
, max(message) as message
, max(substr(message, length(subject)+1)) as message_without_subject
from
general.enhanced_commits
where
length(message) - 100 > length(subject)
and length(subject) > 0
and
commit_timestamp < '2021-01-01' # Enabling reproducibility in the future
group by
commit
;

drop table if exists general.plain_commits_dataset_train;

create table
general.plain_commits_dataset_train
as
select
repo_name
, commit
, subject
, message
, message_without_subject
from
general.plain_commits_dataset
where
dataset_type = 'Train'
;

drop table if exists general.plain_commits_dataset_test;

create table
general.plain_commits_dataset_test
as
select
repo_name
, commit
, subject
, message
, message_without_subject
from
general.plain_commits_dataset
where
dataset_type = 'Test'
;

drop table if exists general.plain_commits_dataset_validation;

create table
general.plain_commits_dataset_validation
as
select
repo_name
, commit
, subject
, message
, message_without_subject
from
general.plain_commits_dataset
where
dataset_type = 'Validation'
;

drop table if exists general.mp_not_corrective_commits;

create table
general.mp_not_corrective_commits
as
select
repo_name
, commit
, general.bq_dataset_type(commit) as dataset_type
, subject
, message
, substr(message, length(subject)+1) as message_without_subject
from
general.plain_commits_dataset
where
# Semantic condition
not general.bq_corrective(message) > 0 # not identified as a bug
and general.bq_core_bug(message) > 0 # Functions hash 4b76d8e76af938824f91f4b99247731c21e37ff9
                                     # Note that this function keeps improving, hence changing
#and
#substr(commit, 8,1) in ('a','8', '6')
#and
#substr(commit, 5,1) in ('1', '3', '4')
;


drop table if exists general.mp_not_refactor_commits;

create table
general.mp_not_refactor_commits
as
select
repo_name
, commit
, general.bq_dataset_type(commit) as dataset_type
, subject
, message
, substr(message, length(subject)+1) as message_without_subject
from
general.plain_commits_dataset
where
# Semantic condition
not general.bq_refactor(message) > 0 # not identified as a refactor
and general.bq_core_refactor(message) > 0 # Functions hash 4b76d8e76af938824f91f4b99247731c21e37ff9
                                     # Note that this function keeps improving, hence changing
#and
#substr(commit, 8,1) in ('a','8', '6')
#and
#substr(commit, 5,1) in ('1', '3', '4')
;


drop table if exists general.mp_not_adaptive_commits_batch_1;

create table
general.mp_not_adaptive_commits_batch_1
as
select
repo_name
, commit
, general.bq_dataset_type(commit) as dataset_type
, subject
, message
, substr(message, length(subject)+1) as message_without_subject
from
general.plain_commits_dataset
where
# Semantic condition
not general.bq_adaptive(message) > 0 # not identified as a adaptive
and general.bq_core_adaptive(message) > 0 # Functions hash 4b76d8e76af938824f91f4b99247731c21e37ff9
                                     # Note that this function keepד improving, hence changing
and
substr(commit, 8,1) in ('2','4', '6', '8', 'a')
;