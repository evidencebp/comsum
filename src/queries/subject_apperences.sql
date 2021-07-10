# into commits_and_subjects_stats.csv
select
count(*) as commits
, count(distinct subject) as  subjects
, count(distinct subject)/count(*) as subject_per_commits
from
general.plain_commits_dataset
;


# into subject_appearance_dist.csv
select
appearance
, count(*) subjects
from
(
select subject
, count(*) as appearance
from
general.plain_commits_dataset
group by
subject
)
group by
appearance
order by
appearance
;

# into common_subjects.csv
select subject
, count(*) as appearance
from
general.plain_commits_dataset
group by
subject
having
count(*) > 10
order by
appearance desc
;

# into commits_and_message_stats.csv
select
count(*) as commits
, count(distinct message) as  messages
, count(distinct message)/count(*) as message_per_commits
from
general.plain_commits_dataset
;

# into message_appearance_dist.csv
select
appearance
, count(*) messages
from
(
select message
, count(*) as appearance
from
general.plain_commits_dataset
group by
message
)
group by
appearance
order by
appearance
;

# into common_messages.csv
select message
, count(*) as appearance
from
general.plain_commits_dataset
group by
message
having
count(*) > 10
order by
appearance desc
;
