#!/bin/sh
# Variables
HOME_DIR="/ebio/abt1_share/prediction_hendecads"
DRIVER_DIR="/ebio/abt3_projects/software"

# Activate conda environments
. /ebio/abt1_share/prediction_hendecads/conda/miniconda3/etc/profile.d/conda.sh
export PATH="/ebio/abt1_share/prediction_hendecads/conda/miniconda3/bin:$PATH"

conda activate "$HOME_DIR/conda/envs/deepcoil"

export PATH="$PATH:$DRIVER_DIR/cuda-11.7/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$DRIVER_DIR/cuda-11.7/lib64:$DRIVER_DIR/cuda-drivers"

echo $(which conda)    

python code/ss_pred/seq2ss.py
