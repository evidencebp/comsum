from os.path import join
import pandas as pd

from rouge_score import rouge_scorer

from configuration import DATA_PATH, COMMITS_SAMPLES, COMMITS_SAMPLES_METIRCS, RELATED_COMMITS_SAMPLES\
, RELATED_COMMITS_SAMPLES_METIRCS, SEMANTIC_COMMITS_SAMPLES, SEMANTIC_NO_SUB_COMMITS_SAMPLES_METIRCS\
    , COMMITS_NO_SUB_SAMPLES_METIRCS, RELATED_FIXES_SAMPLES, RELATED_FIXES_SAMPLES_METIRCS



from feature_pair_analysis import pretty_print


# TODO - message without_subject message_without_subject
# TODO - semantic
def compute_message_text_benchmark():
    df = pd.read_csv(join(DATA_PATH
                            , COMMITS_SAMPLES))

    benchmarks_df = compute_text_metrics(df
        , original_text= 'message'
        , summary= 'subject'
        , administrative_columns = {'repo_name', 'commit'}
        , output_file=join(DATA_PATH
                                , COMMITS_SAMPLES_METIRCS))

def compute_message_no_sub_text_benchmark():
    df = pd.read_csv(join(DATA_PATH
                            , COMMITS_SAMPLES))

    benchmarks_df = compute_text_metrics(df
        , original_text= 'message_without_subject'
        , summary= 'subject'
        , administrative_columns = {'repo_name', 'commit'}
        , output_file=join(DATA_PATH
                                , COMMITS_NO_SUB_SAMPLES_METIRCS))


def compute_related_commits_benchmark():
    df = pd.read_csv(join(DATA_PATH
                            , RELATED_COMMITS_SAMPLES))

    benchmarks_df = compute_text_metrics(df
        , original_text= 'message1'
        , summary= 'subject2'
        , administrative_columns = {'repo_name', 'commit1', 'commit2'}
        , output_file=join(DATA_PATH
                                , RELATED_COMMITS_SAMPLES_METIRCS))


def compute_related_corrective_commits_benchmark():
    df = pd.read_csv(join(DATA_PATH
                            , RELATED_FIXES_SAMPLES))

    benchmarks_df = compute_text_metrics(df
        , original_text= 'message1'
        , summary= 'subject2'
        , administrative_columns = {'repo_name', 'commit1', 'commit2'}
        , output_file=join(DATA_PATH
                                , RELATED_FIXES_SAMPLES_METIRCS))

def compute_text_metrics(df: pd.DataFrame
                         , original_text: str = 'message'
                         , summary: str = 'subject'
                         , administrative_columns = {}
                         , output_file: str = None):

    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = []

    for _, i in df.iterrows():
        #cur_score = scorer.score(i[original_text]
        #                         , i[summary])
        cur_score = scorer.score(i[summary]
                                 , i[original_text])

        for k in administrative_columns:
            score_dict = {k : i[k]}

        score_dict.update(score_to_dict(cur_score))
        scores.append(score_dict)

    benchmarks_df = pd.DataFrame(scores)

    if output_file:
        benchmarks_df.to_csv(output_file
                             , index=False)

    return benchmarks_df

def score_to_dict(score):
    
    res = {'rouge1_precision' : score['rouge1'].precision
        , 'rouge1_recall' : score['rouge1'].recall
        , 'rouge1_fmeasure' : score['rouge1'].fmeasure
        , 'rouge2_precision' : score['rouge2'].precision
        , 'rouge2_recall' : score['rouge2'].recall
        , 'rouge2_fmeasure' : score['rouge2'].fmeasure
        , 'rougeL_precision' : score['rougeL'].precision
        , 'rougeL_recall' : score['rougeL'].recall
        , 'rougeL_fmeasure' : score['rougeL'].fmeasure
    }

    return res

def describe_metrics_df(df: pd.DataFrame):
    metrics = {'rows' : len(df)
                , 'rouge1_precision_mean' : df['rouge1_precision'].mean()
                , 'rouge1_precision_std' : df['rouge1_precision'].std()
                , 'rouge1_recall_mean' : df['rouge1_recall'].mean()
                , 'rouge1_recall_std' : df['rouge1_recall'].std()
                , 'rouge1_fmeasure_mean' : df['rouge1_fmeasure'].mean()
                , 'rouge1_fmeasure_std' : df['rouge1_fmeasure'].std()

                , 'rouge2_precision_mean': df['rouge2_precision'].mean()
                , 'rouge2_precision_std': df['rouge2_precision'].std()
                , 'rouge2_recall_mean': df['rouge2_recall'].mean()
                , 'rouge2_recall_std': df['rouge2_recall'].std()
                , 'rouge2_fmeasure_mean': df['rouge2_fmeasure'].mean()
                , 'rouge2_fmeasure_std': df['rouge2_fmeasure'].std()

                , 'rougeL_precision_mean': df['rougeL_precision'].mean()
                , 'rougeL_precision_std': df['rougeL_precision'].std()
                , 'rougeL_recall_mean': df['rougeL_recall'].mean()
                , 'rougeL_recall_std': df['rougeL_recall'].std()
                , 'rougeL_fmeasure_mean': df['rougeL_fmeasure'].mean()
                , 'rougeL_fmeasure_std': df['rougeL_fmeasure'].std()

               }
    return metrics

def describe_file_metrics(metrics_file):
    df = pd.read_csv(metrics_file)
    metrics = describe_metrics_df(df)
    pretty_print(metrics)

    return metrics


def describe_message_text_benchmark():
    return describe_file_metrics(join(DATA_PATH
                            , COMMITS_SAMPLES_METIRCS))

def describe_related_commits_benchmark():
    return describe_file_metrics(join(DATA_PATH
                            , RELATED_COMMITS_SAMPLES_METIRCS))

def describe_related_fixes_benchmark():
    return describe_file_metrics(join(DATA_PATH
                            , RELATED_FIXES_SAMPLES_METIRCS))



def compute_message_no_sub_semantic_benchmark():
    df = pd.read_csv(join(DATA_PATH
                            , SEMANTIC_COMMITS_SAMPLES))

    benchmarks_df = compute_text_metrics(df
        , original_text= 'message_without_subject'
        , summary= 'subject'
        , administrative_columns = {'repo_name', 'commit'}
        , output_file=join(DATA_PATH
                                , SEMANTIC_NO_SUB_COMMITS_SAMPLES_METIRCS))


if __name__ == "__main__":

    print("Subject vs. message benchmark")
    compute_message_text_benchmark()
    metrics = describe_message_text_benchmark()
    print(r"\newcommand \mainDataSetSize {"+ str(metrics['rows']) +"}")
    print(r"\newcommand \subjectvsMessageRougeOne {"+ str(round(metrics['rouge1_fmeasure_mean'], 2)) +"}")
    print(r"\newcommand \subjectvsMessageRougeL {"+ str(round(metrics['rougeL_fmeasure_mean'], 2)) +"}")

    print("Subject vs. message without subject benchmark")
    compute_message_no_sub_text_benchmark()
    metrics = describe_file_metrics(join(DATA_PATH
                               , COMMITS_NO_SUB_SAMPLES_METIRCS))
    print(r"\newcommand \noSubjectvsMessageRougeOne {"+ str(round(metrics['rouge1_fmeasure_mean'], 2)) +"}")
    print(r"\newcommand \nosubjectvsMessageRougeL {"+ str(round(metrics['rougeL_fmeasure_mean'], 2)) +"}")

    print("Related commits benchmark")
    compute_related_commits_benchmark()
    metrics = describe_related_commits_benchmark()
    print(r"\newcommand \relatedCommitRougeOne {"+ str(round(metrics['rouge1_fmeasure_mean'], 2)) +"}")
    print(r"\newcommand \relatedCommitRougeL {"+ str(round(metrics['rougeL_fmeasure_mean'], 2)) +"}")


    print("Related fixes benchmark")
    compute_related_corrective_commits_benchmark()
    metrics = describe_related_fixes_benchmark()
    print(r"\newcommand \relatedFixesRougeOne {"+ str(round(metrics['rouge1_fmeasure_mean'], 2)) +"}")
    print(r"\newcommand \relatedFixesRougeL {"+ str(round(metrics['rougeL_fmeasure_mean'], 2)) +"}")

    print("Subject vs. message without subject benchmark on semantic")
    compute_message_no_sub_semantic_benchmark()
    metrics = describe_file_metrics(join(DATA_PATH
                               , SEMANTIC_NO_SUB_COMMITS_SAMPLES_METIRCS))
