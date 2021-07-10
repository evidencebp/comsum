from os.path import join
import pandas as pd

from configuration import DATA_PATH

LABELED_FILE = 'cumsum_random_batch_9_july_2021.csv'
LABELED_FILE_WITH_DISTANCE = 'cumsum_random_batch_9_july_2021_with_distance.csv'

administrative_terms = ['Acked-by:',
 'Change-Id:',
 'Commit-Queue:',
 'Committed:',
 'Continuous-Integration:',
 'Cr-Commit-Position:',
 'Cr-Original-Commit-Position:',
 'Former-commit-id:',
 'GitOrigin-RevId:',
 'git-svn-id:',
 'ORIGINAL_AUTHOR=',
 'Review-Url:',
 'Reviewed-by:',
 'Reviewed-on:',
 'Signed-off-by:',
 'Tested-by: ']



NOT_FOUND = -1
CLOSE_ENOUGH = 20
def administrative_distance(text):
    occurences = [text.find(i) for i in administrative_terms if text.find(i) != NOT_FOUND]

    if len(occurences):
        return min(occurences)
    else:
        return NOT_FOUND

def is_administrative(text):
    distance = administrative_distance(text)

    return distance != NOT_FOUND and distance <= CLOSE_ENOUGH

def manual_test_adminstrative_distance():
    tests = {'123' : -1
             , '123Committed:' : 3}

    for i in tests.keys():
        print("test:"
              , i
              , "expected"
              , tests[i]
              , "result"
              , administrative_distance(i)
              , "pass"
              , tests[i] == administrative_distance(i))

def evaluate_distance():

    CONTENT_COL = 'message_without_subject'
    DISTANCE_COL = 'distance'
    ADMINISTRATIVE_COL = 'administrative_pred'
    df = pd.read_csv(join(DATA_PATH
                          , LABELED_FILE))

    df[DISTANCE_COL] = df[CONTENT_COL].map(administrative_distance)
    df[ADMINISTRATIVE_COL] = df[CONTENT_COL].map(is_administrative)
    print(df[DISTANCE_COL].value_counts(normalize=True).sort_index()[:50])
    print(df[df[ADMINISTRATIVE_COL]][['commit', 'message_without_subject', DISTANCE_COL]])

    print(df[df['Comment'] == 'Administrative message'][['commit', DISTANCE_COL]])

    df.to_csv(join(DATA_PATH
                          , LABELED_FILE_WITH_DISTANCE)
                , index=False)


if __name__ == "__main__":
    #manual_test_adminstrative_distance()
    evaluate_distance()