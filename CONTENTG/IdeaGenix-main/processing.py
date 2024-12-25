import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Load dataset from file
def load_dataset(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()
    return data

# Tokenize and preprocess the data
def preprocess_data(data):
    # Tokenize the data
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(data)
    total_words = len(tokenizer.word_index) + 1
    
    # Create input sequences using tokenized data
    input_sequences = []
    for line in data:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)
    
    # Pad sequences to ensure uniform input size
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
    
    # Split inputs and labels
    xs, labels = input_sequences[:,:-1],input_sequences[:,-1]
    
    # One-hot encode labels
    ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)
    
    return xs, ys, max_sequence_len, total_words, tokenizer

