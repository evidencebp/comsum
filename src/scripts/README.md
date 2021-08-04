administrative_message_identifier.py - some commit messages (other then the title) are just administrative (e.g., not describing the change content by the reviwer).
Such commits are not suitable for text summarization and the follwing file is a labeling function for identifying them.

filter_messages.py  - After opening the zip files, this splits the data to have a test of separate time and repositories

build_benchmarks.py	- Builds the none machine learning benchmark - entire messgae, related fix, etc.

configuration.py	- common constants, directory locations, etc.

convert_csv.py		- convert csvs into the format of data huggingface expects (a folder with files names train\val\test.source\target)

evaluate_concept_stability.py - evaluates meaning preserving per concept.

evaluate_meaning_preserving.py - evaluate meaning preserving.

finetune_distillbart_comsum.sh - an examples of finetuning a model with tokenizers library

requirements.txt - pyhton libraries used in this project
