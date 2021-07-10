# Extract samples of the data sets using the pseudo-random commit hash.
# This way one get reproducability with having to freeze samples too.
# The selection is choosen in order to get data sets of about 10k samples

drop table if exists general.test_sample_b1;

create table
general.test_sample_b1
as
select
*
from
general.plain_commits_dataset
where
dataset_type = 'Test'
and
substr(commit, 8,1) in ('1')
and
 substr(commit, 9,1) in ('2', '4','6', '8', 'a', 'c')
;



drop table if exists general.train_sample_b1;

create table
general.train_sample_b1
as
select
*
from
general.plain_commits_dataset
where
dataset_type = 'Train'
and
substr(commit, 8,1) in ('1')
and
substr(commit, 9,1) in ('2')
and
substr(commit, 10,1) in ('1', '2', '4','6', '8', 'a', 'c')
;



drop table if exists general.mp_not_corrective_commits_sample_b1;

create table
general.mp_not_corrective_commits_sample_b1
as
select
*
from
general.mp_not_corrective_commits
where
dataset_type = 'Test'
and
substr(commit, 10,1) in ('1', '2', '3', '4', '5', '6', '7','8', '9', 'a', 'c')
;


drop table if exists general.mp_not_refactor_commits_sample_b1;

create table
general.mp_not_refactor_commits_sample_b1
as
select
*
from
general.mp_not_refactor_commits
where
dataset_type = 'Test'
#and
#substr(commit, 10,1) in ('1', '2', '3', '4', '5', '6', '7','8', '9', 'a', 'c')
;


drop table if exists general.mp_not_adaptive_commits_sample_b1;

create table
general.mp_not_adaptive_commits_sample_b1
as
select
*
from
general.mp_not_adaptive_commits_batch_1
where
dataset_type = 'Test'
#and
#substr(commit, 10,1) in ('1', '2', '3', '4', '5', '6', '7','8', '9', 'a', 'c')
;