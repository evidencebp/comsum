import sys

ANALYSIS_PATH = '/Users/idan/src/analysis_utils'
sys.path.append(ANALYSIS_PATH)


LANGUAGE_PATH = '/Users/idan/src/commit-classification'
sys.path.append(LANGUAGE_PATH)

BASE_PATH = r'/Users/idan/src/Commit-Summarization/'
DATA_PATH = BASE_PATH + r'data/'
FIGURES_PATH = BASE_PATH + r'figures/'
PERFORMANCE_PATH = BASE_PATH + r'performance/'
MODELS_PATH = BASE_PATH + r'models/'

COMMITS_SAMPLES = 'commits_batch1.csv'
COMMITS_SAMPLES_METIRCS = 'commits_batch1_metrics.csv'
COMMITS_NO_SUB_SAMPLES_METIRCS = 'commits_no_sub_batch1_metrics.csv'

RELATED_COMMITS_SAMPLES = 'related_train_sample_b1.csv'
RELATED_COMMITS_SAMPLES_METIRCS = 'related_commits_metrics.csv'

RELATED_FIXES_SAMPLES = 'related_corrective_train_sample_b1.csv'
RELATED_FIXES_SAMPLES_METIRCS = 'related_corrective_commits_metrics.csv'


SEMANTIC_COMMITS_SAMPLES = 'semmantic_commits_batch1.csv'
SEMANTIC_NO_SUB_COMMITS_SAMPLES_METIRCS = 'semmantic_commits_batch1_nosub_metrics.csv'

SEMANTIC_COMMITS_SUMMARY = 'semmantic_commits_batch1_summary.txt'
