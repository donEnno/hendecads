import argparse

import pandas as pd
from sklearn.model_selection import StratifiedKFold
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping        # type: ignore

from binary_model.model import build_binary_lstm_model, build_binary_cnn_model
from utils import tokenize_binary_data, Logger

tf.config.threading.set_inter_op_parallelism_threads(32)
tf.config.threading.set_intra_op_parallelism_threads(32)


# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--max_seq_len', type=int, default=512, help='Maximum sequence length')
parser.add_argument('--batch_size', type=int, default=32, help='Batch size')
parser.add_argument('--epochs', type=int, default=5, help='Number of epochs')
parser.add_argument('--model', type=str, default='lstm', help='Model type')
parser.add_argument('--target', type=str, default='3R_hendecad_strict', help='Target column')
args = parser.parse_args()

df = pd.read_csv('/ebio/abt1_share/prediction_hendecads/1_repo/2_ss_pred/dataset/annotated_df.csv')

# only use stretch_seq that are shorter than max_seq_len
df = df[df.stretch_seq.str.len() <= args.max_seq_len]

X, n_words = tokenize_binary_data(df, max_seq_len=args.max_seq_len)
y = (df['3R_hendecad_strict'] > 1).to_numpy()

cv = StratifiedKFold(n_splits=5, random_state=777, shuffle=True)

c = 0
for ix, (tr_ix, val_ix) in enumerate(cv.split(X, y)):
    c += 1
    print('CV fold: %s' % c)
    
    if args.model == 'lstm':
        model = build_binary_lstm_model(n_words, max_seq_len=args.max_seq_len)
    if args.model == 'cnn':
        model = build_binary_cnn_model(n_words, max_seq_len=args.max_seq_len)

    logger = Logger(X[val_ix], y[val_ix], optimize='auc')

    
    model.fit(X[tr_ix], y[tr_ix], 
              batch_size=args.batch_size, 
              epochs=args.epochs, 
              verbose=1,
              callbacks=logger)
    
    model.save(f'models/{args.model}_{args.target}_{ix}.keras')
