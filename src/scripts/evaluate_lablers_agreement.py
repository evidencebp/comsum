from os.path import join
import pandas as pd

from configuration import DATA_PATH
from agreement_utils import compute_agreement


def compute_lablers_agreement(first_df
                      , second_df
                      , concept
                      , common_columns):

    FIRST_CONCEPT = concept + '_1'
    SECOND_CONCEPT = concept + '_2'

    first_df[FIRST_CONCEPT]   = first_df[concept].astype(bool)
    second_df[SECOND_CONCEPT] = second_df[concept].astype(bool)

    joint = pd.merge(first_df[common_columns + [FIRST_CONCEPT]]
                     , second_df[common_columns + [SECOND_CONCEPT]]
                     , on=common_columns)

    agreement = len(joint[joint[FIRST_CONCEPT] == joint[SECOND_CONCEPT]])/len(joint)

    return joint, agreement

def compute_summary_agreement(first_file
                              , second_file
                              , disagreements_file):
    concept = 'Is_Summary'
    first_df = pd.read_csv(first_file)
    second_df = pd.read_csv(second_file)

    joint, agreement =  compute_lablers_agreement(first_df
                      , second_df
                      , concept=concept
                      , common_columns=['repo_name', 'commit', 'subject', 'message_without_subject'])

    print("agrement", agreement)
    joint[joint[concept + '_1'] != joint[concept + '_2']].to_csv(disagreements_file
                                                                 , index=False)
if __name__ == "__main__":

    LABELS_PATH = DATA_PATH + '/labels/'
    compute_summary_agreement(first_file=join(LABELS_PATH, 'cum_sumrandom_batch_9_july_2021_labels.csv')
                              , second_file=join(LABELS_PATH, '2ann_cum_sumrandom_batch_9_july_2021_labels.csv')
                              , disagreements_file=join(LABELS_PATH, 'cum_sumrandom_batch_9_july_2021_disagree.csv'))

