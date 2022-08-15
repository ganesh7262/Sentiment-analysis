from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.lang.en import English
import emoji
import spacy
from sklearn.preprocessing import OneHotEncoder
from sklearn.utils.validation import check_is_fitted
from sklearn.model_selection import train_test_split
from sklearn.exceptions import NotFittedError
import numpy as np
import re

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stopwords = set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm")

class Preprocessor:
    def __init__(self, stopwords=stopwords):
        self.vectorizer = TfidfVectorizer(lowercase=False, max_features=8000,
                                         min_df=10, ngram_range=(1, 3),
                                         tokenizer=None)
        self.stopwords = stopwords
        self.vectorizer_fitted = False
        
    
        
    def transform(self, X, y=None, mode='train'):
        def remove_urls(self, texts):
            print('Removing URLs...')
            pattern = re.compile('(\w+\.com ?/ ?.+)|(http\S+)')
            return [re.sub(pattern, '', text) for text in texts]
    
        def remove_double_space(self, texts):
            print('Removing double space...')
            pattern = re.compile(' +')
            return [re.sub(pattern, ' ', text) for text in texts]
            
        def remove_punctuation(self, texts):
            print('Removing Punctuation...')
            pattern = re.compile('[^a-z ]')
            return [re.sub(pattern, ' ', text) for text in texts]
        
        def remove_stopwords(self, texts):
            print('Removing stopwords...')
            return [[w for w in text.split(' ') if w not in self.stopwords] for text in tqdm(texts)]
        
        def remove_numbers(self, texts):
            print('Removing numbers...')
            return [' '.join([w for w in text if not w.isdigit()]) for text in tqdm(texts)]
        
        def decode_emojis(self, texts):
            print('Decoding emojis...')
            return [emoji.demojize(text, language='en') for text in texts] 
        
        def lemmatize(self, texts):
            print('Lemmatizing...')
            lemmatized_texts = []
            for text in tqdm(texts):
                doc = nlp(text)
                lemmatized_texts.append(' '.join([token.lemma_ for token in doc]))
                                        
            return lemmatized_texts
        X = X.copy()
        print('Removing Nans...')
        X = X[~X.isnull()]                          # delete nans
        X = X[~X.duplicated()]                      # delete duplicates
        
        if mode == 'train':
            self.train_idx = X.index
        else:
            self.test_idx = X.index
        print('Counting capitalized...')
        capitalized = [np.sum([t.isupper() for t in text.split()]) 
                           for text in np.array(X.values)]  # count capitalized
        # X['cap'] = capitalized
        print('Lowering...')
        X = [text.lower() for text in X]             # lower
        X = self.remove_urls(X)                      # remove urls
        X = self.remove_punctuation(X)               # remove punctuation
        X = self.remove_double_space(X)              # remove double space
        X = self.decode_emojis(X)                    # decode emojis
        X = self.remove_stopwords(X)                 # remove stopwords
        X = self.remove_numbers(X)                   # remove numbers                      
        X = self.lemmatize(X)                        # lemmatize
        
        if not self.vectorizer_fitted:
            self.vectorizer_fitted = True
            print('Fitting vectorizer...')
            self.vectorizer.fit(X)

        print('Vectorizing...')
        X = self.vectorizer.transform(X)             # vectorize
        
        return X