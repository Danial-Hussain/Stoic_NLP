# -*- coding: utf-8 -*-
"""Processing.ipynb

# Data Preprocessing

The aim of this notebook is to gather the data and clean it for the model to use during training.

**First I will Import any relevant libraries**
"""

#Import all relevant libraries
import pandas as pd
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
import seaborn as sns

# Neural Net Preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences

#Unzip uploaded file
# !unzip NLP.zip

"""**Next I will import the data generated from the python scripts into the jupyter notebook**"""

#Loading in the data
def load_data(directory):
    discourses = pd.read_csv("{}/discourses.csv".format(directory))
    enchiridion = pd.read_csv("{}/enchiridion.csv".format(directory))
    golden_sayings = pd.read_csv("{}/golden_sayings.csv".format(directory))
    letters = pd.read_csv("{}/letters.csv".format(directory))
    meditations = pd.read_csv("{}/meditations.csv".format(directory))
    return discourses, enchiridion, golden_sayings, letters, meditations

"""**Function to join all the data together and convert the values to a list**"""

#Joining the data together
def join(d,e,g,l,m):
    combined = pd.concat([d,e,g,l,m])
    length = 'There are a total of {} sentences from stoic philosophers'.format(len(combined))
    null = "There is a total of {} null values".format(len(combined) - (combined['Lesson'].isnull().value_counts()[0]))
    val = combined['Lesson'].values.tolist()
    val = [x.lower() for x in val]
    return length, null, combined, val

def average_length(data):
    total_length = sum([len(x) for x in data['Lesson']])
    num_elements = len(data)
    avg_len = total_length//num_elements
    avg_len = avg_len//5
    return avg_len

"""Arranging the data for the model

First I will tokenize the data. This removes punctuation, makes all the text into lowercase and splits up the words assigning them to numbers. This is an important step as computers are better at reading numbers than text.
"""

def tokenize(data):
    data = data['Lesson']
    max_words = 35000
    tokenizer = Tokenizer(num_words = max_words)
    tokenizer.fit_on_texts(data.values)
    sequences = tokenizer.texts_to_sequences(data.values)
    print(sequences[:5])
    return sequences, tokenizer


def flatten(sequences, tokenizer):
    text = [item for sublist in sequences for item in sublist]
    vocab_size = len(tokenizer.word_index)
    print("Vocab size: {}".format(vocab_size))
    return vocab_size, text

def sliding_window(text, tokenizer):
    # Training certain amount of words and predicting next
    sentence_len = 20
    pred_len = 1
    train_len = sentence_len - pred_len
    seq = []
    # Sliding window to generate train data
    for i in range(len(text)-sentence_len):
        seq.append(text[i:i+sentence_len])
    # Reverse dictionary to decode tokenized sequences back to words
    reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))

    trainX = []
    trainy = []
    for i in seq:
        trainX.append(i[:train_len])
        trainy.append(i[-1])
    return trainX, trainy, train_len, reverse_word_map

"""Now I'll define one function that calls all the other functions"""

def complete():
    string = 'Stoicism NLP/data'
    d, e, g, l, m = load_data(string)
    l, n, combined, val = join(d,e,g,l,m)
    avg_len = average_length(combined)
    sequences, tokenizer = tokenize(combined)
    vocab_size, text = flatten(sequences, tokenizer)
    trainX, trainy, train_len, reverse_word_map = sliding_window(text, tokenizer)
    return sequences, vocab_size, text, trainX, trainy, train_len, tokenizer, reverse_word_map, avg_len
    
sequences, vocab_size, text, trainX, trainy, train_len, tokenizer, reverse_word_map, avg_len = complete()

