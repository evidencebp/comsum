#!/bin/bash
#SBATCH --mem=32g
#SBATCH -c4
#SBATCH --time=7-0
#SBATCH --gres=gpu:4,vmem:8g
#SBATCH --mail-type=BEGIN,END,FAIL,TIME_LIMIT
#SBATCH --mail-user=leshem.choshen@mail.huji.ac.il
#SBATCH --output=/cs/snapless/oabend/borgr/comsum/slurm/cmsm%j.out

echo "start"
#module load tensorflow
module load cuda
module load cudnn/7.6.2
module load nccl/2.4.8
source /cs/snapless/oabend/borgr/envs/sm/bin/activate

model_name_or_path=sshleifer/distilbart-cnn-12-6
#model_name_or_path=/cs/snapless/oabend/borgr/comsum/transformers/output/distillbart5m/
comsum_dir=/cs/snapless/oabend/borgr/comsum
dirpath=$comsum_dir/transformers/examples/seq2seq/
cd $dirpath
basedir=$dirpath/../../
data_dir=$basedir/../Commit-Summarization/data/train5m
output_dir=$basedir/output/distillbart5m
weights_save_path=$output_dir/weights
max_source_length=512
overwrite_output_dir=""
overwrite_output_dir="--overwrite_output_dir"
mkdir $output_dir -p
export PYTHONPATH="${dirpath}/../":"${PYTHONPATH}"
# From appendix C of paper https://arxiv.org/abs/1912.08777
# Set --gradient_accumulation_steps  so that effective batch size is 256 (2*128, 4*64, 8*32, 16*16)

echo python $dirpath/finetune.py \
    --data_dir=$data_dir \
    --learning_rate=1e-4 \
    --model_name_or_path $model_name_or_path \
    --output_dir=$output_dir \
    $overwrite_output_dir \
    --do_train \
    --do_predict \
    --gpus 4 \
    --n_val 1000 \
    --val_check_interval 0.1 \
    --train_batch_size=2 \
    --eval_batch_size=2 \
    --gradient_accumulation_steps 128\
    --max_source_length $max_source_length --max_target_length 128 \
    --freeze_embeds --label_smoothing 0.1 --adafactor --task summarization_comsum \
    --weights_save_path $weights_save_path\
    --save_top 4\
    "$@"
#    --resume_from_checkpoint checkp

python $dirpath/finetune.py \
    --data_dir=$data_dir \
    --learning_rate=1e-4 \
    --model_name_or_path $model_name_or_path \
    --output_dir=$output_dir \
    $overwrite_output_dir \
    --do_train \
    --do_predict \
    --gpus 4 \
    --n_val 1000 \
    --val_check_interval 0.25 \
    --train_batch_size=2 \
    --eval_batch_size=2 \
    --gradient_accumulation_steps 128\
    --max_source_length $max_source_length --max_target_length 128 \
    --freeze_embeds --label_smoothing 0.1 --adafactor --task summarization_comsum \
    --weights_save_path $weights_save_path\
    --save_top 4\
    "$@"
#    --resume_from_checkpoint checkp

echo "done"