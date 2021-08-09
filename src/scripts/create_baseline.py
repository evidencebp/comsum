import os
import random

import pandas as pd
import re

from configuration import DATA_PATH, BASE_PATH, SPLIT_DATA_PATH

sentence_splitter = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s")


def random_sentence_choice(inpath, outpath, force):
    if os.path.isfile(outpath) and not force:
        print(f"{outpath} already exists pass force =True to overwrite")
        return
    print(f"reading {os.path.abspath(inpath)}")
    print(f"writing to  {os.path.abspath(outpath)}")
    with open(inpath) as lines:
        with open(outpath, "w") as outfl:
            for document in lines:
                sentences = sentence_splitter.split(document)
                sentences = [sentence for sentence in sentences if sentence]
                outfl.write(random.choice(sentences).strip() + "\n")


if __name__ == '__main__':
    force = False
    force = True
    working_dir = os.path.join(DATA_PATH, "split")
    outdir = os.path.join(BASE_PATH, "outputs", "random")
    os.makedirs(outdir, exist_ok=True)
    # inpath = os.path.join(SPLIT_DATA_PATH,"train1batch","/train.source")
    # outpath = os.path.join(outdir, "train1batch.txt")
    # random_sentence_choice(inpath, outpath, force=force)

    # inpath = os.path.join(SPLIT_DATA_PATH,"semantic","train.source")
    # outpath = os.path.join(outdir, "semantic.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"train_short","train.source")
    # outpath = os.path.join(outdir, "train_short.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"adaptive","train.source")
    # outpath = os.path.join(outdir, "adaptive.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"corrective","train.source")
    # outpath = os.path.join(outdir, "corrective.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"refactor","train.source")
    # outpath = os.path.join(outdir, "refactor.txt")
    # random_sentence_choice(inpath, outpath, force=force)

    # inpath = os.path.join(SPLIT_DATA_PATH,"train5m","train.source")
    # outpath = os.path.join(outdir, "train5m.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"train1m","train.source")
    # outpath = os.path.join(outdir, "train1m.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"train2m","train.source")
    # outpath = os.path.join(outdir, "train2m.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"train","train.source")
    # outpath = os.path.join(outdir, "train.txt")
    # random_sentence_choice(inpath, outpath, force=force)

    # inpath = os.path.join(SPLIT_DATA_PATH,"train_short","train.source")
    # outpath = os.path.join(outdir, "train_short.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"train","test.source")
    # outpath = os.path.join(outdir, "test.txt")
    # random_sentence_choice(inpath, outpath, force=force)

    # inpath = os.path.join(SPLIT_DATA_PATH,"adaptive10","train.source")
    # outpath = os.path.join(outdir, "adaptive10.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"corrective10","train.source")
    # outpath = os.path.join(outdir, "corrective10.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"refactor10","train.source")
    # outpath = os.path.join(outdir, "refactor10.txt")
    # random_sentence_choice(inpath, outpath, force=force)

    # inpath = os.path.join(SPLIT_DATA_PATH,"test_sample","test.source")
    # outpath = os.path.join(outdir, "test_sample.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"train_sample","train.source")
    # outpath = os.path.join(outdir, "train_sample.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"adaptive_sample","test.source")
    # outpath = os.path.join(outdir, "adaptive_sample.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"corrective_sample","test.source")
    # outpath = os.path.join(outdir, "corrective_sample.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH,"refactor_sample","test.source")
    # outpath = os.path.join(outdir, "refactor_sample.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH, "test", "test.source")
    # outpath = os.path.join(outdir, "test.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    #
    # inpath = os.path.join(SPLIT_DATA_PATH, "train", "train.source")
    # outpath = os.path.join(outdir, "train.txt")
    # random_sentence_choice(inpath, outpath, force=force)
    inpath = os.path.join(SPLIT_DATA_PATH, "test_sample", "test.source")
    outpath = os.path.join(outdir, "test_sample.txt")
    random_sentence_choice(inpath, outpath, force=force)

    inpath = os.path.join(SPLIT_DATA_PATH, "train_sample", "train.source")
    outpath = os.path.join(outdir, "train_sample.txt")
    random_sentence_choice(inpath, outpath, force=force)
