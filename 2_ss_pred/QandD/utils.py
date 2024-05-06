import tensorflow as tf
from keras.utils import to_categorical, pad_sequences       # type: ignore
from tensorflow.keras.preprocessing.text import Tokenizer   # type: ignore
import numpy as np
from keras import callbacks
from sklearn.metrics import average_precision_score, roc_auc_score, f1_score, precision_score, recall_score


def tokenize_binary_data(df, max_seq_len=1024):
    
    tokenizer_in = Tokenizer(char_level=True)
    tokenizer_in.fit_on_texts(df.stretch_seq)
             
    X = tokenizer_in.texts_to_sequences(df.stretch_seq)
    X = pad_sequences(X, maxlen=max_seq_len, padding='post')

    n_words = len(tokenizer_in.word_index) + 1

    return X, n_words


class Logger(callbacks.Callback):
    def __init__(self, val_X, val_y, optimize='f1', save=True):
        """
        Logger for predictors build with ml-toolbox
        :param val_X: 
        :param val_y:
        :param out_path: Out path for model weights
        :param out_fn: Filename of the out weights
        :param optimize: Metric to optimize. Available: "f1", "auc", "auprc"
        :param f1_cutoff:
        :param save:
        :param nni:
        """
        super(Logger, self).__init__()

        self.opt_metric = 0
        self.optimize = optimize
        self.val_X = val_X
        self.val_y = val_y
        self.save = save
        self.improvement = True

    def on_epoch_end(self, epoch, logs=None):
        if logs is None:
            logs = {}

        y_pred = self.model.predict(self.val_X)
        y_true = self.val_y

        # Compute metrics
        auc = roc_auc_score(y_true, y_pred)
        auprc = average_precision_score(y_true, y_pred)

        y_pred[y_pred >= 0.5] = 1
        y_pred[y_pred < 0.5] = 0

        f1 = f1_score(y_true, y_pred)
        sens = recall_score(y_true, y_pred)
        prec = precision_score(y_true, y_pred)

        if self.optimize == 'auc':
            metric = auc
        elif self.optimize == 'auprc':
            metric = auprc
        else:
            metric = f1

        # Check if there was an improvement over last best value of optimized metric
        improvement = self.opt_metric < metric

        if improvement:
            self.opt_metric = metric
        else:
            self.improvement = improvement

        print('AUC: {}, AUPRC: {}, F1: {}, SENS: {}, PREC: {}, BEST: {}'.format('%.3f' % auc,
                                                                                '%.3f' % auprc,
                                                                                '%.3f' % f1,
                                                                                '%.3f' % sens,
                                                                                '%.3f' % prec,
                                                                                improvement))

        if not self.improvement: 
            self.model.stop_training = True

        return
