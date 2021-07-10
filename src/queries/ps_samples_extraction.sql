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

# Extracts the data set for commit summarization

drop table if exists general.related_train_sample_b1;

create table
general.related_train_sample_b1
as
select
pair.*
, pair_details.subject  as subject2
, pair_details.message  as message2

from
(
select
ec1.repo_name
, ec1.commit as commit1
, max(ec2.commit) as commit2
, max(ec1.author_name) as author_name
, max(ec1.subject)  as subject1
, max(ec1.message)  as message1
from
general.enhanced_commits as ec1
join
general.train_sample_b1 as d1
on
ec1.repo_name = d1.repo_name
and
ec1.commit = d1.commit
join
general.enhanced_commits as ec2
on
ec1.repo_name = ec2.repo_name
and
ec1.author_name = ec2.author_name
and
abs(TIMESTAMP_DIFF(ec1.commit_timestamp, ec2.commit_timestamp, day)) <= 7
join
general.plain_commits_dataset as d2
on
ec2.repo_name = d2.repo_name
and
ec2.commit = d2.commit
group by
ec1.repo_name
, ec1.commit
) as pair
join
general.enhanced_commits as pair_details
on
pair.repo_name = pair_details.repo_name
and
pair.commit2 = pair_details.commit

;


drop table if exists general.related_corrective_train_sample_b1;

create table
general.related_corrective_train_sample_b1
as
select
pair.*
, pair_details.subject  as subject2
, pair_details.message  as message2

from
(
select
ec1.repo_name
, ec1.commit as commit1
, max(ec2.commit) as commit2
, max(ec1.author_name) as author_name
, max(ec1.subject)  as subject1
, max(ec1.message)  as message1
from
general.enhanced_commits as ec1
join
general.train_sample_b1 as d1
on
ec1.repo_name = d1.repo_name
and
ec1.commit = d1.commit
join
general.enhanced_commits as ec2
on
ec1.repo_name = ec2.repo_name
and
ec1.author_name = ec2.author_name
and
abs(TIMESTAMP_DIFF(ec1.commit_timestamp, ec2.commit_timestamp, day)) <= 7
join
general.plain_commits_dataset as d2
on
ec2.repo_name = d2.repo_name
and
ec2.commit = d2.commit
where
ec1.is_corrective
and
ec2.is_corrective
group by
ec1.repo_name
, ec1.commit
) as pair
join
general.enhanced_commits as pair_details
on
pair.repo_name = pair_details.repo_name
and
pair.commit2 = pair_details.commit

;