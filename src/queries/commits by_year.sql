# into commits_by_year.csv
select
extract(year from ec.commit_timestamp) as year
, count(distinct d.commit) as commits
, count(*) as samples
from
general.plain_commits_dataset as d
join
general.enhanced_commits as ec
on
d.repo_name = ec.repo_name
and
d.commit = ec.commit
group by
year
order by
year desc
;
