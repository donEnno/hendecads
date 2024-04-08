import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
import re

from Bio import SeqIO

import tensorflow as tf
from keras import backend  as K
from keras.models import Model
from keras import Input
from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Bidirectional
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical, pad_sequences
from sklearn.model_selection import train_test_split

from utils import plot_prediction, plot_confusion_matrix

# ------------------------------------------------------------------------------
# Device configuration

if os.getcwd() == '/home/enno/uni/SS23/thesis':
    file_path = '/home/enno/uni/SS23/thesis/data/ss_data/seq.csv'
else:
    file_path = '/ebio/abt1_share/prediction_hendecads/data/ss_pred/seq.csv'

# ------------------------------------------------------------------------------
# Data

MAX_SEQ_LEN = 4096

def load_data(file_path=file_path, max_seq_len=MAX_SEQ_LEN):
    df = pd.read_csv(file_path)
    df = df[(df.seq.str.len() <= max_seq_len) & (~df.has_nonstd_aa)]    

    return df


# def load_hendecads_data(file_path=file_path,
#               max_seq_len=2048):
      # Uses data from New Protein Families

#     fasta_sequences = SeqIO.parse(open(file_path), 'fasta')
#     n_seq = len(list(fasta_sequences))

#     df = pd.DataFrame(columns=['id', 'seq', 'stretch_ix'])

#     pattern = r'\[\[.*?\]\]'

#     for seq_ix, seq in enumerate(SeqIO.parse(open(file_path), 'fasta')):
#         print(f"Processing sequence {seq_ix+1}/{n_seq}", end='\r')

#         if len(seq.seq) > max_seq_len:
#             continue
        
#         s = str(seq.seq)
#         d = str(seq.description)
        
#         # Finds string in seq.description that matches CC stretches
#         stretches = eval(re.findall(pattern, d.split('|||')[-1])[0])
#         cc_ix = [int(x) for stretch in stretches for x in np.arange(stretch[0], stretch[1]+1)]
        
#         df.loc[len(df)] = [seq.id, s, str(cc_ix)]  # Why needs this to be a sting?

#     df['seq_mask'] = df['seq'].apply(lambda seq: ''.join(['C' if s_i.islower() else 'X' for s_i in seq]))

#     return df
        

def tokenize_data(df, 
                  max_seq_len=MAX_SEQ_LEN, data_flavor='kaggel'):
    
    tokenizer_in = Tokenizer(char_level=True)
    tokenizer_in.fit_on_texts(df.seq)
    
    tokenizer_out = Tokenizer(char_level=True)
    
    if data_flavor == 'kaggel':
        tokenizer_out.fit_on_texts(df.sst3)
        y = tokenizer_out.texts_to_sequences(df.sst3)    
        
    if data_flavor == 'hendecads':
        tokenizer_out.fit_on_texts(df.seq_mask)
        y = tokenizer_out.texts_to_sequences(df.seq_mask)    
        
    X = tokenizer_in.texts_to_sequences(df.seq)
    X = pad_sequences(X, maxlen=max_seq_len, padding='post')

    y = pad_sequences(y, maxlen=max_seq_len, padding='post')
    y = to_categorical(y)

    n_words = len(tokenizer_in.word_index) + 1
    n_tags = len(tokenizer_out.word_index) + 1

    return X, y, n_words, n_tags


def split_data(X, y, 
               test_size=0.2, val_size=0.5, random_state=42):
    
    X_train, X_, y_train, y_ = train_test_split(X, y, test_size=test_size, random_state=random_state, shuffle=True)
    X_val, X_test, y_val, y_test = train_test_split(X_, y_, test_size=val_size, random_state=random_state, shuffle=True)
    
    return X_train, X_val, X_test, y_train, y_val, y_test

# ------------------------------------------------------------------------------
# Model

def build_model(n_words, n_tags, 
<<<<<<< HEAD
                max_seq_len=2048):
=======
                max_seq_len=MAX_SEQ_LEN):
>>>>>>> f0f3c94e34f2a422a7820c520daf8fe3bcafa01a
    
    input = Input(shape=(max_seq_len,))
    
    mbed = Embedding(input_dim=n_words, output_dim=128, input_length=max_seq_len)(input)
    comp = Bidirectional(LSTM(units=64, return_sequences=True, recurrent_dropout=0.1))(mbed)
    
    final_comp = TimeDistributed(Dense(n_tags, activation="softmax"))(comp)
    
    model = Model(input, final_comp)
    
    return model


def train_model(model, X_train, X_val, y_train, y_val, 
                batch_size=32, epochs=5):
    
    def q3_acc(y_true, y_pred):
        y = tf.argmax(y_true, axis=-1)
        y_ = tf.argmax(y_pred, axis=-1)
        mask = tf.greater(y, 0)
        return K.cast(K.equal(tf.boolean_mask(y, mask), tf.boolean_mask(y_, mask)), K.floatx())

    model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy", q3_acc])
    
    model.fit(X_train, y_train, 
              batch_size=batch_size, 
              epochs=epochs, 
              validation_data=(X_val, y_val), 
              verbose=1)

    return model

# ------------------------------------------------------------------------------
# Main

if __name__ == '__main__':
    print("Loading data...")
    df = load_data()

    print("Tokenizing data...")
    X, y, n_words, n_tags = tokenize_data(df)

    print("Splitting data...")
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)

    print("Building model...")
    model = build_model(n_words, n_tags)
    model.summary()

    print("Training model...")
    model = train_model(model, X_train, X_val, y_train, y_val)
    model.evaluate(X_test, y_test)

    print("Plotting predictions...")
    y_pred = model.predict(X_test[1:2])
    
    plot_prediction(y_pred, y_test[1:2], fig_path='/ebio/abt1_share/prediction_hendecads/data/ss_pred/plot_pred.csv')
    plot_confusion_matrix(1, y_pred, y_test[1:2], fig_path='/ebio/abt1_share/prediction_hendecads/data/ss_pred/plot_pred.csv')
