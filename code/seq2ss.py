import tensorflow as tf

from keras import backend  as K
from keras.models import Model
from keras import Input
from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Bidirectional
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical, pad_sequences

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

import os

# Load the data
def load_data(file_path='/ebio/abt1_share/prediction_hendecads/data/seq2ss_data/seq.csv',
              max_seq_len=256,
              test_size=0.2,
              random_state=42):

    df = pd.read_csv(file_path)
    df = df[(df.seq.str.len() <= max_seq_len) & (~df.has_nonstd_aa)]
    