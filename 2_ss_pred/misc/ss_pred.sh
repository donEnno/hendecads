#!/bin/sh

# Activate conda
. /ebio/abt1_share/prediction_hendecads/conda/miniconda3/etc/profile.d/conda.sh
conda activate tf38

python /ebio/abt1_share/prediction_hendecads/1_repo/2_ss_pred/seq2ss.py