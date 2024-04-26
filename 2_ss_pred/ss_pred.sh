#!/bin/sh

# Variables
HOME_DIR="/ebio/abt1_share/surfaceome"
DRIVER_DIR="/ebio/abt3_projects/software" 

. /ebio/abt1_share/prediction_hendecads/conda/miniconda3/etc/profile.d/conda.sh
conda activate tf
HOME_DIR="/ebio/abt1_share/surfaceome"
DRIVER_DIR="/ebio/abt3_projects/software" 

export PATH="$PATH:$DRIVER_DIR/cuda-11.7/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$DRIVER_DIR/cuda-11.7/lib64:$DRIVER_DIR/cuda-drivers" 

python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
# python /ebio/abt1_share/prediction_hendecads/1_repo/02_ss_pred/seq2ss.py