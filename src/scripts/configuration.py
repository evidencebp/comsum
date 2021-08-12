import sys
import os

ANALYSIS_PATH = '/Users/idan/src/analysis_utils'
sys.path.append(ANALYSIS_PATH)



BASE_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
# e.g. BASE_PATH = r'/Users/idan/src/comsum/'
sys.path.append(BASE_PATH)

DATA_PATH = os.path.join(BASE_PATH, r'data')
SAMPLED_DATA_PATH = os.path.join(DATA_PATH, r'samples')
FULL_DATA_PATH = os.path.join(DATA_PATH, r'dataset')
SAMPLES_PATH = os.path.join(DATA_PATH, r'samples')
SPLIT_DATA_PATH = os.path.join(DATA_PATH, r'split')
AUX_DATA_PATH = os.path.join(DATA_PATH, r'aux_datasets')
LABELS_PATH = os.path.join(DATA_PATH, r'labels')
FIGURES_PATH = os.path.join(BASE_PATH, r'figures')
PERFORMANCE_PATH = os.path.join(BASE_PATH, r'performance')
MODELS_PATH = os.path.join(BASE_PATH, r'models')

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

MERGE_COMMIT_FILES = 'comsum_merge_commits.csv'
SPLIT_FILE = 'repos_split.csv'