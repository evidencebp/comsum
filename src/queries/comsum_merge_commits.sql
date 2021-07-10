drop table if exists general.comsum_merge_commits;


create table
general.comsum_merge_commits
as
select
ec.commit
from
general.plain_commits_dataset as d
join
general.enhanced_commits as ec
on
d.repo_name = ec.repo_name
and
d.commit = ec.commit
where
parents > 1
group by
ec.commit
;