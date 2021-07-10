"""
Evaluate the stability of a SE concept over a random sample, not a meaning preserving one.
"""

import pandas as pd
import configuration

from df_to_latex_table import df_to_latex_table
from file_utils import prefix_columns

from adaptive_model import is_core_adaptive, is_adaptive
from corrective_model import is_core_bug, is_fix
from refactor_model import built_is_refactor, is_core_refactor

key = ['line']
signature_columns = ['Is Core Bug', 'Is Bug', 'Is Core Refactor', 'Is Refactor', 'Is Core Adaptive'
            , 'Is Adaptive']

def classify_file(file_name
                  , message_signature_file):

    with open(file_name) as f:
        content = f.readlines()

    line = 0
    rows = []
    for i in content:
        line += 1
        rows.append([line
                     , is_core_bug(i) > 0
                     , is_fix(i) > 0
                     , is_core_refactor(i) > 0
                     , built_is_refactor(i) > 0
                     , is_core_adaptive(i) > 0
                     , is_adaptive(i) > 0
                     ])

    df = pd.DataFrame(rows
                      , columns=key + signature_columns)

    if message_signature_file:
        df.to_csv(message_signature_file
                    , index=False)
    return df

def evaluate_concept_stability(message_signature_file
                               , summary_signature_file):

    MESSAGE_PREFIX = 'message'
    SUMMARY_PREFIX = 'summary'

    message_df = pd.read_csv(message_signature_file)
    summary_df = pd.read_csv(summary_signature_file)

    message_df = prefix_columns(message_df
                   , prefix=MESSAGE_PREFIX
                   , columns=set(message_df.columns) - set(key))
    summary_df = prefix_columns(summary_df
                   , prefix=SUMMARY_PREFIX
                   , columns=set(summary_df.columns) - set(key))

    joint = pd.merge(message_df
                     , summary_df
                     , on=key
                     )

    preserving = {}
    for i in signature_columns:
        preserving[i] = len(joint[(joint[MESSAGE_PREFIX + i] == True) & (joint[SUMMARY_PREFIX + i] == True)])/(
            len(joint[(joint[MESSAGE_PREFIX + i] == True)]))

    return preserving

def run_evaluate_concept_stability():

    DATA_PATH = '~/Downloads/'
    message_file = DATA_PATH + 'train.source'
    bart_file = DATA_PATH +'test_bart.txt'
    zshot_bart_file = DATA_PATH + 'test_zshot_bart.txt'

    message_signature_file = DATA_PATH +'message_signature.csv'
    bart_signature_file = DATA_PATH +'bart_signature.csv'
    zshot_bart_signature_file = DATA_PATH +'zshot_bart_signature.csv'


    df = classify_file(message_file
                       , message_signature_file)
    #print(df)

    df = classify_file(bart_file
                       ,bart_signature_file)
    #print(df)

    df = classify_file(zshot_bart_file
                       ,zshot_bart_signature_file)
    #print(df)

    bart_preserving = evaluate_concept_stability(message_signature_file
                               , summary_signature_file=bart_signature_file)
    bart_preserving['Model'] = 'Bart'
    #print(bart_preserving)

    zshot_bart_preserving = evaluate_concept_stability(message_signature_file
                               , summary_signature_file=zshot_bart_signature_file)
    zshot_bart_preserving['Model'] = 'Zero-Shot Bart'
    #print(zshot_bart_preserving)

    pres_df = pd.DataFrame([bart_preserving, zshot_bart_preserving]
                           , columns= ['Model'] +signature_columns)

    print()
    df_to_latex_table(
        pres_df
        , caption='\label{tab:test-semmantic-corrective} Meaning Preserving on Test'
#        , columns_header="{ | l| l| p{15mm}| p{15mm}| p{15mm}| p{15mm}| p{15mm}  | }"
        , rounding_digits=2)
    print()


if __name__ == "__main__":
    run_evaluate_concept_stability()