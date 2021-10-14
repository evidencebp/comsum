from os.path import join
import pandas as pd

from configuration import OUTPUTS_PATH, AUX_DATA_PATH, MERGE_COMMIT_FILES

from administrative_message_identifier import label_df_as_administrative, ADMINISTRATIVE_COL
from df_to_latex_table import df_to_latex_table

from adaptive_model import is_core_adaptive, is_adaptive
from corrective_model import is_core_bug, is_fix
from refactor_model import built_is_refactor, is_core_refactor

MEANING_COLUMN = 'is_bug'

CORE_COLUMN = 'is_core_bug'

summaries = [{'model' : 'Bart'
                , 'dataset' : 'Corrective'
                , 'file': join(OUTPUTS_PATH, 'mp_corrective_bart.txt')
                 , 'core_classifier' : is_core_bug
                , 'meaning_classifier' : is_fix
                }
              , {'model' : 'Bart'
                , 'dataset' : 'Refactor'
                ,'file': join(OUTPUTS_PATH, 'mp_refactor_bart.txt')
                 , 'core_classifier' : is_core_refactor
                , 'meaning_classifier' : built_is_refactor
                }
            , {'model' : 'Bart'
                , 'dataset' : 'Adaptive'
                ,'file': join(OUTPUTS_PATH, 'mp_adaptive_bart.txt')
                         , 'core_classifier': is_core_adaptive
                         , 'meaning_classifier': is_adaptive
               }
             ]

def evaluate_meaning_preserving(summary_file: str
                                , core_classifier
                                , meaning_classifier):
    # Using readlines()
    file = open(summary_file, 'r')
    Lines = file.readlines()

    stats = []
    line_count = 0
    # Strips the newline character
    for line in Lines:
        stats.append((line_count
                      , line
                      , bool(core_classifier(line) > 0)
                      , bool(meaning_classifier(line) > 0)))

        line_count += 1

    df = pd.DataFrame(stats
                      , columns=['line'
            , 'message_without_subject' # This is really the output. Use the name hardcoded in filtering
            , CORE_COLUMN, MEANING_COLUMN])
    print("original df", len(df))

    # Removing administrative commits
    filtered_df = label_df_as_administrative(df)
    filtered_df = filtered_df[(filtered_df[ADMINISTRATIVE_COL] == False)]
    df = filtered_df
    print("filtered df", len(df))


    df[CORE_COLUMN] = df[CORE_COLUMN].astype(bool)
    df[MEANING_COLUMN] = df[MEANING_COLUMN].astype(bool)

    """
    g = df.groupby([CORE_COLUMN, MEANING_COLUMN], as_index=False).agg({'line': 'count'})

    columns_to_name = {CORE_COLUMN: 'Is Core Bug'
        , MEANING_COLUMN: 'Is Bug'
                       }

    print()
    df_to_latex_table(
        g
        , caption='\label{tab:semmantic-corrective}'
        , columns_to_name=columns_to_name
        , rounding_digits=0)
    print()

    print(df.is_core_bug.value_counts(normalize=True))
    print(df.is_bug.value_counts(normalize=True))
    """

    stats = {'core_and_meaning' : len(df[(df[CORE_COLUMN] > 0) & (df[MEANING_COLUMN] > 0)])/len(df)
             , 'not_core_and_meaning': len(df[(df[CORE_COLUMN] == 0) & (df[MEANING_COLUMN] > 0)])/len(df)
             , 'core_and_not_meaning': len(df[(df[CORE_COLUMN] > 0) & (df[MEANING_COLUMN] == 0)])/len(df)
             , 'not_core_and_not_meaning': len(df[(df[CORE_COLUMN] == 0) & (df[MEANING_COLUMN] == 0)])/len(df)
             }

    return stats


def analyze_summaries():

    all_stats = []
    for summary in summaries:
        #print(summary['file'])
        stats = evaluate_meaning_preserving(summary['file']
                                    , core_classifier=summary['core_classifier']
                                    , meaning_classifier=summary['meaning_classifier']
                                    )
        stats['Model'] = summary['model']
        stats['dataset'] = summary['dataset']
        print(stats)
        all_stats.append(stats)

    df = pd.DataFrame(all_stats)
    #df = pd.DataFrame(all_stats
    #                  , columns=['Core and Meaning', 'Not Core and Meaning', 'Core and Not Meaning'
    #        , 'Not Core and Not Meaning', 'Model', 'Dataset']).sort_values(['Model', 'Dataset'])
    #features_df = pd.DataFrame(rows
    #                           , columns=['Metric', 'Hit Rate', 'High Quality', 'Low Quality'  # , 'Mean', 'CMean'
    #                                      ]).sort_values('Metric')

    df['Not Preserved'] = df['not_core_and_meaning'] + df['core_and_meaning']
    print()
    df_to_latex_table(
        df[['Model', 'dataset', 'Not Preserved', 'core_and_meaning', 'not_core_and_meaning', 'core_and_not_meaning', 'not_core_and_not_meaning'  ]]
        , caption='\label{tab:semmantic-corrective} Meaning Preserving'
        , columns_to_name={'core_and_meaning' : 'Core and Concept'
             , 'not_core_and_meaning': 'Not Core and Concept'
             , 'core_and_not_meaning': 'Core and Not Concept'
             , 'not_core_and_not_meaning': 'Not Core and Not Concept'
             , 'dataset' : 'Data set'
             }
        , columns_header="{ | l| l| p{15mm}| p{15mm}| p{15mm}| p{15mm}| p{15mm}  | }"
        , rounding_digits=2)
    print()

if __name__ == "__main__":
    analyze_summaries()