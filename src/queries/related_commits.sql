# Extracts the data set for commit summarization

drop table if exists general.related_commits_batch2;

create table
general.related_commits_batch2
as
select
ec1.repo_name
, ec1.commit as commit1
, ec2.commit as commit2
, ec1.author_name
, ec1.subject  as subject1
, ec1.message  as message1
, ec2.subject  as subject2
, ec2.message  as message2
from
general.enhanced_commits as ec1
join
general.plain_commits_dataset as d1
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
and
ec1.commit > ec2.commit # The break symmetry in order not to get each pair as (A,B) and (B, A)
join
general.plain_commits_dataset as d2
on
ec2.repo_name = d2.repo_name
and
ec2.commit = d2.commit
order by
rand()
limit 10000
;


drop table if exists general.related_corrective_commits_batch2;

create table
general.related_corrective_commits_batch2
as
select
ec1.repo_name
, ec1.commit as commit1
, ec2.commit as commit2
, ec1.author_name
, ec1.subject  as subject1
, ec1.message  as message1
, ec2.subject  as subject2
, ec2.message  as message2
from
general.enhanced_commits as ec1
join
general.plain_commits_dataset as d1
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
and
ec1.commit > ec2.commit # The break symmetry in order not to get each pair as (A,B) and (B, A)
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
order by
rand()
limit 10000
;