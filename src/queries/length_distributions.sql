
# into subject_len_dist.csv
select
length(subject) as len
, count(*) as commits
from
general.plain_commits_dataset
group by
len
order by
len
;

# into message_without_subject_len_dist.csv
select
length(message_without_subject) as len
, count(*) as commits
from
general.plain_commits_dataset
group by
len
order by
len
;

# into subject_ratio_dist.csv
select
round(length(subject)/length(message_without_subject),2) as ratio
, count(*) as commits
from
general.plain_commits_dataset
group by
ratio
order by
ratio
;

# into subject_words_dist.csv
select
length(subject) - LENGTH(REGEXP_REPLACE(subject, ' ', '')) + 1 as words
, count(*) as commits
from
general.plain_commits_dataset
group by
words
order by
words
;

# into message_without_subject_words_dist.csv
select
length(message_without_subject) - LENGTH(REGEXP_REPLACE(message_without_subject, ' ', '')) + 1 as words
, count(*) as commits
from
general.plain_commits_dataset
group by
words
order by
words
;

# into subject_word_ratio_dist.csv
select
round((length(subject) - LENGTH(REGEXP_REPLACE(subject, ' ', '')) + 1)/
(length(message_without_subject) - LENGTH(REGEXP_REPLACE(message_without_subject, ' ', '')) + 1),2) as ratio
, count(*) as commits
from
general.plain_commits_dataset
group by
ratio
order by
ratio
;
