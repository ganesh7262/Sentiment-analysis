import re
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from tqdm import tqdm
from spacy.lang.en import English
import emoji
import nltk

class Preprocess:
    def __init__(self) -> None:
        self.vectorizer=TfidfVectorizer(lowercase=False,max_features=10000,min_df=10,ngram_range=(1,3),tokenizer=None)
        nltk.download('stopwords')
        self.stopwords=set(stopwords.words('english'))
        self.vectorizer_fitted=False
        self.nlp = spacy.load("en_core_web_sm")

    def remove_urls(self,texts):
        print("removing urls...")
        pattern = re.compile('(\w+\.com ?/ ?.+)|(http\S+)')
        return [re.sub(pattern,'',text) for text in texts]

    def remove_double_space(self,texts):
        print("removing doule space...")
        pattern=re.compile(' +')
        return [re.sub(pattern,'',text) for text in texts]
    
    def remove_punctuation(self,texts):
        print("removing punctuations....")
        pattern = re.compile('[^a-z ]')
        return [re.sub(pattern,"",text) for text in texts]
    
    def remove_stopwords(self,texts):
        print("removing stopwords...")
        return [[w for w in text.split() if w not in self.stopwords] for text in tqdm(texts)]

    def remove_numbers(self,texts):
        print("removing numbers....")
        return [' '.join([w for w in text if not w.isdigit()]) for text in tqdm(texts)]

    def decode_emojis(self,texts):
        print("decoding emojis...")
        return [emoji.demojize(text,language='en') for text in texts]
    
    def lammatiaze(self,texts):
        print("lammatizing...")
        lammaztized_text=[]
        for text in tqdm(texts):
            doc=self.nlp(text)
            lammaztized_text.append(' '.join([token.lemma_ for token in doc]))

        return lammaztized_text