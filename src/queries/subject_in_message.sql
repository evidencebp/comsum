# into common_messages.csv
select
count(*)
, sum(if(message_without_subject	like concat('%', subject, '%'), 1,0)) as subject_in_message
, sum(if(message_without_subject	like concat('%', subject, '%'), 1,0))/count(*) as subject_in_message_ratio
from
general.plain_commits_dataset

;

# into common_extractive_subjects.csv
select subject
, count(*) as appearance
from
general.plain_commits_dataset
where
message_without_subject	like concat('%', subject, '%')
group by
subject
having
count(*) > 10
order by
appearance desc
;

select
count(*)
, sum(if(regexp_contains(subject, 'merge'), 1,0)) as merge_branch
, sum(if(regexp_contains(subject, 'merge'), 1,0))/count(*) as merge_branch_ratio
from
general.plain_commits_dataset

;
