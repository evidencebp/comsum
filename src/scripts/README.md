administrative_message_identifier.py - some commit messages (other then the title) are just administrative (e.g., not describing the change content by the reviwer).
Such commits are not suitable for text summarization and the follwing file is a labeling function for identifying them.

build_benchmarks.py	- Builds the none machine learning benchmark - entire messgae, related fix, etc.

configuration.py	- common constants, directory locations, etc.

convert_csv.py		

evaluate_concept_stability.py - evaluates meaning preserving per concept.

evaluate_meaning_preserving.py - evaluate meaning preserving.

finetune_distillbart_comsum.sh

requirments.txt - pyhton libraries used in this project