
select
count(distinct commit) as commits

, sum(if(general.bq_corrective(message) > 0,1,0))/count(distinct commit) as corrective_hits_ratio
, sum(if(general.bq_core_bug(message) > 0,1,0))/count(distinct commit) as core_corrective_hits_ratio
, sum(if(general.bq_corrective(message) > 0 and general.bq_core_bug(message) > 0,1,0))/sum(if(general.bq_core_bug(message) > 0,1,0)) as conditional_corrective

, sum(if(general.bq_refactor(message) > 0,1,0))/count(distinct commit) as refactor_hits_ratio
, sum(if(general.bq_core_refactor(message) > 0,1,0))/count(distinct commit) as core_refactor_hits_ratio
, sum(if(general.bq_refactor(message) > 0 and general.bq_core_refactor(message) > 0,1,0))/sum(if(general.bq_core_refactor(message) > 0,1,0)) as conditional_refactor

, sum(if(general.bq_adaptive(message) > 0,1,0))/count(distinct commit) as adaptive_hits_ratio
, sum(if(general.bq_core_adaptive(message) > 0,1,0))/count(distinct commit) as core_adaptive_hits_ratio
, sum(if(general.bq_adaptive(message) > 0 and general.bq_core_adaptive(message) > 0,1,0))/sum(if(general.bq_core_adaptive(message) > 0,1,0)) as conditional_adaptive


from
general.plain_commits_dataset_test
;