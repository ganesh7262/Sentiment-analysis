import re
import emoji

class Preprocessor:
    
    def remove_urls (text):
        return re.sub('http://\S+|https://\S+', '', text)
    
    
    def remove_non_ascii(self,text):
        return re.sub(r'[^\x00-\x7f]',r'', text)
    
    def remove_punct(self,text):
        return re.sub(r'[]!"$%&\'()*+,./:;=#@?[\\^_`{|}~-]+', "", text)
    
    def emoji_handeling(self,text):
        txt=emoji.demojize(text)
        txt=txt.replace(':',' ')
        txt=txt.replace('_',' ')
        txt=txt.split('_')
        return ''.join(txt)
    
    def call_all_func(self,X):
        X=self.emoji_handeling(X)
        X=self.remove_urls(X)
        X=self.remove_non_ascii(X)
        X=self.remove_punct(X)

        return X



    

