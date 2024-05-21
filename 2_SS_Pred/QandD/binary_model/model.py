import tensorflow as tf
from tensorflow.keras import backend  as K                                                  # type: ignore
from tensorflow.keras.models import Model                                                   # type: ignore                      
from tensorflow.keras import Input                                                          # type: ignore
from tensorflow.keras.layers import LSTM, Embedding, Dense, TimeDistributed, Bidirectional  # type: ignore
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten                           # type: ignore


def build_binary_lstm_model(n_words, max_seq_len):
    input = Input(shape=(max_seq_len,))
    
    mbed = Embedding(input_dim=n_words, output_dim=128)(input)
    comp = Bidirectional(LSTM(units=16, return_sequences=False, recurrent_dropout=0.1))(mbed)
    
    final_comp = Dense(1, activation="sigmoid")(comp)
    
    model = Model(input, final_comp)

    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy", "AUC"])
    
    return model


def build_binary_cnn_model(n_words, max_seq_len):
    input = Input(shape=(max_seq_len,))
    
    mbed = Embedding(input_dim=n_words, output_dim=128)(input)
    conv = Conv1D(filters=128, kernel_size=5, activation='relu')(mbed)
    pool = MaxPooling1D(pool_size=5)(conv)
    flat = Flatten()(pool)
    comp = Dense(128, activation='relu')(flat)
    
    final_comp = Dense(1, activation="sigmoid")(comp)
    
    model = Model(input, final_comp)

    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy", "AUC"])
    
    return model
