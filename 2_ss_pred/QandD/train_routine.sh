#!/bin/sh

# Activate conda
. /ebio/abt1_share/prediction_hendecads/conda/miniconda3/etc/profile.d/conda.sh
conda activate tf_cpu

for model in "cnn" "lstm"; do
    echo "Training model: $model"

    for target in "3R" "5R" "7R"; do
        echo "Training target: $target"
        python /ebio/abt1_share/prediction_hendecads/1_repo/2_ss_pred/QandD/train.py --model="$model" --target="${target}_hendecad_strict"
    done
done