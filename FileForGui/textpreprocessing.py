# utilities
import re
import pickle
import numpy as np
import pandas as pd

import string, unicodedata
import contractions 
import inflect

# nltk

from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
STOPWORDS = set(stopwords.words('english'))

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
STOPWORDS = set(stopwords.words('english'))

# Defining dictionary containing all emojis with their meanings.
emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad', 
          ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
          ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed', 
          ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
          '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
          '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink', 
          ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}


def to_lowercase(text):
    text=text.lower()
    return text

def remove_URL(text):
    """Remove URLs from a sample string"""
    return re.sub(r"http\S+", "", text)

def replace_contractions(text):
    """Replace contractions in string of text"""
    text = contractions.fix(text)
    return text

def cleaning_hashtag(text):
    return re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])",' ',text)

def cleaning_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

# Cleaning and removing the above emojis list from the tweet text
def cleaning_emojis(text):
    return " ".join([word for word in str(text).split() if word not in emojis])

def replace_numbers(text):
    return re.sub('[0-9]+', '', text)

def remove_punctuation(text):
  return  re.sub(r'[^\w\d\s]', ' ',text)


# processing of text
def normalize(text):
  text = to_lowercase(text)
  text = remove_URL(text)
  text = replace_contractions(text)
  text = cleaning_hashtag(text)
  text = cleaning_stopwords(text)
  text = cleaning_emojis(text)
  text = replace_numbers(text)
  text = remove_punctuation(text)
  return text

def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def combine_single(words):
    words = " ".join(words)
    return words

#preprocessing of text
def process_text(text_data):
    text_data = normalize(text_data)
    text_data= text_data.split()
    text_data= stem_words(text_data)
    text_data= lemmatize_verbs(text_data)
    text_data= combine_single(text_data)

    return text_data
