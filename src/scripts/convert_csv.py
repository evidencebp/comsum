import os

import pandas as pd
import re


def normalize(string):
    if not isinstance(string, str):
        print(f"string? {string}")
    string = re.sub(r"\s+", " ", string.strip())
    while "  " in string:
        string = string.replace("  ", " ")
    return string


def csv_to_data(work_dir, out_dir, csv_paths, val_size=1000, test_size=1000, force=False):
    if not force and os.path.isdir(out_dir):
        print(f"Skipping, pass force=True to overwrite. Dir exists {os.path.abspath(out_dir)}")
        return
    os.makedirs(out_dir, exist_ok=True)
    dfs = []
    for csv_path in csv_paths:
        df = pd.read_csv(f"{csv_path}")
        dfs.append(df)
    df = pd.concat(dfs)
    df["message_without_subject"] = df["message_without_subject"].apply(normalize)
    df["subject"] = df["subject"].apply(normalize)
    if "dataset_type" in df.columns:
        with open(os.path.join(out_dir, "train.source"), "w") as fl:
            source_lines = df[df["dataset_type"] == "Train"]["message_without_subject"]
            fl.write("\n".join([line for line in source_lines if line]))
        with open(os.path.join(out_dir, "train.target"), "w") as fl:
            target_lines = df[df["dataset_type"] == "Train"]["subject"]
            assert len(target_lines) == len(source_lines), f"lengths {len(target_lines), len(source_lines)}"
            fl.write("\n".join([line for line in target_lines if line]))
        with open(os.path.join(out_dir, "val.source"), "w") as fl:
            source_lines = df[df["dataset_type"] == "Validation"]["message_without_subject"]
            fl.write("\n".join([line for line in source_lines if line]))
        with open(os.path.join(out_dir, "val.target"), "w") as fl:
            target_lines = df[df["dataset_type"] == "Validation"]["subject"]
            assert len(target_lines) == len(source_lines), f"lengths {len(target_lines), len(source_lines)}"
            fl.write("\n".join([line for line in target_lines if line]))
        with open(os.path.join(out_dir, "test.source"), "w") as fl:
            source_lines = df[df["dataset_type"] == "Test"]["message_without_subject"]
            fl.write("\n".join([line for line in source_lines if line]))
        with open(os.path.join(out_dir, "test.target"), "w") as fl:
            target_lines = df[df["dataset_type"] == "Test"]["subject"]
            assert len(target_lines) == len(source_lines), f"lengths {len(target_lines), len(source_lines)}"
            fl.write("\n".join([line for line in target_lines if line]))
            return

    print(f"writing to {os.path.abspath(out_dir)}")
    with open(f"{work_dir}/messages", "w") as messages_fl:
        with open(f"{work_dir}/subjects", "w") as subjects_fl:
            for idx, row in df.iterrows():
                try:
                    message = row["message_without_subject"]
                    subject = row["subject"]
                    if message and subject:
                        messages_fl.write(message + "\n")
                        subjects_fl.write(subject + "\n")
                except AttributeError as e:
                    print(f"Error in line:{idx, row['message_without_subject']}\n{row['subject']}")
                    # if row["message_len"] < 4:
                    #     print("message", message)
                    #     print("subject", subject)
                    # if row["subject_len"] < 4:
                    #     print("message", message)
                    #     print("subject", subject)

    with open(f"{work_dir}/messages") as source_fl:
        with open(f"{work_dir}/subjects") as target_fl:
            with open(os.path.join(out_dir, "train.source"), "w") as train_source:
                with open(os.path.join(out_dir, "train.target"), "w") as train_target:
                    with open(os.path.join(out_dir, "val.source"), "w") as val_source:
                        with open(os.path.join(out_dir, "val.target"), "w") as val_target:
                            with open(os.path.join(out_dir, "test.source"), "w") as test_source:
                                with open(os.path.join(out_dir, "test.target"), "w") as test_target:
                                    for i, (source, target) in enumerate(zip(source_fl, target_fl)):
                                        if i < val_size:
                                            val_source.write(source)
                                            val_target.write(target)
                                        elif i < val_size + test_size:
                                            test_source.write(source)
                                            test_target.write(target)
                                        else:
                                            train_source.write(source)
                                            train_target.write(target)


if __name__ == '__main__':
    # force = True
    force = False
    out_dir = "data/train1batch/"
    working_dir = "data"
    csv_path = "data/commits_batch1.csv"
    csv_to_data(working_dir, out_dir, [csv_path])

    out_dir = "data/semantic"
    csv_path = "data/semmantic_commits_batch1.csv"
    csv_to_data(working_dir, out_dir, [csv_path], 0, 0)

    out_dir = "data/adaptive"
    csv_path = "data/mp_not_adaptive_commits_batch1.csv"
    csv_to_data(working_dir, out_dir, [csv_path], 0, 0, force=force)

    out_dir = "data/corrective"
    csv_path = "data/mp_not_corrective_commits_batch1.csv"
    csv_to_data(working_dir, out_dir, [csv_path], 0, 0, force=force)

    out_dir = "data/refactor"
    csv_path = "data/mp_not_refactor_commits_batch1.csv"
    csv_to_data(working_dir, out_dir, [csv_path], 0, 0, force=force)

    out_dir = "data/train5m"
    csv_path = "data/plain_commits_batch1.csv"
    csv_to_data(working_dir, out_dir, [csv_path], force=force)

    out_dir = "data/train1m"
    csv_paths = ["data/plain_commits_batch_1m00000000000" + str(i) for i in range(3)]
    csv_to_data(working_dir, out_dir, csv_paths, force=force)

    out_dir = "data/train2m"
    csv_paths = ["data/plain_commits_batch_2m00000000000" + str(i) for i in range(6)]
    csv_to_data(working_dir, out_dir, csv_paths, force=force)

    force = True
    out_dir = "data/train"
    csv_paths = ["data//Full/Train/plain_commits_dataset_train00000000000" + str(i) for i in range(10)] + ["data//Full/Train/plain_commits_dataset_train0000000000" + str(i) for i in range(10, 16)]
    csv_to_data(working_dir, out_dir, csv_paths, force=force)
