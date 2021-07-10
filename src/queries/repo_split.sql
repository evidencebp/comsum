CREATE OR REPLACE FUNCTION
general.bq_repo_type
 (repo_name string)
 RETURNS string
AS (
    case
        when substr(TO_HEX(md5(repo_name)), 1,1) = '0'  then 'Validation'
        when substr(TO_HEX(md5(repo_name)), 1,1) = '1'  then 'Test'
        else 'Train' end # Train

 )
;


WITH tab AS (
  SELECT  'tensorflow/tensorflow' AS repo_name
            , 'Train' as expected
    UNION ALL SELECT '3846masa/upload-gphotos'
                    , 'Validation'

    UNION ALL SELECT '3scale/echo-api'
                    , 'Test'

    UNION ALL SELECT null
                    , null
)
SELECT repo_name
, expected
, general.bq_repo_type(repo_name) as actual
, general.bq_repo_type(repo_name) = expected as pass
FROM tab as testing
;

drop table if exists general.repos_split;

create table
general.repos_split
as
select
repo_name
, general.bq_repo_type(repo_name) as type
from
general.plain_commits_dataset
group by
repo_name
;

select
type
, count(*) as repos
from
general.repos_split
group by
type
;
