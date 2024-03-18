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


def load_data(file_path='/ebio/abt1_share/prediction_hendecads/data/seq2ss_data/seq.csv',
              max_seq_len=256,
              test_size=0.2,
              random_state=42):

    fasta_sequences = SeqIO.parse(open(file_path), 'fasta')
    n_seq = len(list(fasta_sequences))

    df = pd.DataFrame(columns=['id', 'seq', 'stretch_ix'])

    pattern = r'\[\[.*?\]\]'

    for seq_ix, seq in enumerate(fasta_sequences):
        print(f"Processing sequence {seq_ix+1}/{n_seq}", end='\r')

        if len(seq.seq) > max_seq_len:
            continue
        
        s = str(seq.seq)
        d = str(seq.description)
        
        # Finds string in seq.description that matches CC stretches
        stretches = eval(re.findall(pattern, d.split('|||')[-1])[0])
        cc_ix = [x for stretch in stretches for x in np.arange(stretch[0], stretch[1]+1)]
        
        df.loc[len(df)] = [seq.id, s, cc_ix]

    return df
        











if __name__ == '__main__':
    load_data()