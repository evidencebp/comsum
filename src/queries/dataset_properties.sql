# Legacy Sql
# into bq_description.csv
select
count(distinct repo_name) as repos
, count(*) as commit
, count(distinct commit) as distinct_commits
from
[bigquery-public-data.github_repos.commits]
where
year(USEC_TO_TIMESTAMP(committer.date.seconds*1000000))  <= 2020 # Enabling reproducibility in the future
;

select
count(distinct ec.commit) as commits
, count(distinct if(length(ec.message)  > length(ec.subject) and length(ec.subject) > 0, ec.commit , null)) as proper_commits
, round(1.0*count(distinct if(length(ec.message)  > length(ec.subject) and length(ec.subject) > 0, ec.commit , null))/count(distinct ec.commit), 2) as proper_ratio
, count(distinct ec.repo_name) as repos
, concat("\\newcommand \\projectsNum {", cast(count(distinct ec.repo_name) as string), "}") as projectsNum_command
, count(distinct ec.author_email) as authors
, avg(if(length(ec.message)  > length(ec.subject) and length(ec.subject) > 0, length(ec.message) , null)) as proper_message_avg
, avg(if(length(ec.message)  > length(ec.subject) and length(ec.subject) > 0, length(ec.subject) , null)) as proper_subject_avg
, avg(if(length(ec.message)  > length(ec.subject) and length(ec.subject) > 0, length(ec.message)/length(ec.subject) , null)) as proper_compress_avg

from
general.enhanced_commits as ec
;

select
count(distinct ec.commit) as commits
, count(distinct if(length(ec.message)  > length(ec.subject) and length(ec.subject) > 0, ec.commit , null)) as proper_commits
, round(1.0*count(distinct if(length(ec.message)  > length(ec.subject) and length(ec.subject) > 0, ec.commit , null))/count(distinct ec.commit), 2) as proper_ratio
, count(distinct ec.repo_name) as repos
, concat("\\newcommand \\projectsNum {", cast(count(distinct ec.repo_name) as string), "}") as projectsNum_command
, count(distinct ec.author_email) as authors
, avg(if(length(ec.message)  > length(ec.subject) and length(ec.subject) > 0, length(ec.message) , null)) as proper_message_avg
, avg(if(length(ec.message)  > length(ec.subject) and length(ec.subject) > 0, length(ec.subject) , null)) as proper_subject_avg
, avg(if(length(ec.message)  > length(ec.subject) and length(ec.subject) > 0, length(ec.message)/length(ec.subject) , null)) as proper_compress_avg

, sum(if(is_cursing,1,0)) as swearing
, sum(if(is_negative_sentiment,1,0)) as negative_sentiment
, min(ec.commit_timestamp) as first_commit_timestamp
from
general.plain_commits_dataset as d
join
general.enhanced_commits as ec
on
d.repo_name = ec.repo_name
and
d.commit = ec.commit
;

select
dataset_type
, count(distinct commit) as commits
from
general.plain_commits_dataset as d
group by
dataset_type
;
