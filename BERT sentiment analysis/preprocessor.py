import re
import emoji

class Preprocessor:
    
    def remove_urls (self,text):
        return  re.sub(r"https:(\/\/t\.co\/([A-Za-z0-9]|[A-Za-z]){10})", "", text)
    
    def remove_mentions(self,text):
        return re.sub(r"@[A-Za-z0-9_]+","", text)
    
    # def remove_non_ascii(self,text):
    #     return re.sub(r'[^\x00-\x7f]',r'', text)
    
    def remove_punct(self,text):
        return re.sub(r'[]!"$%&\'()*+,./:;=#@?[\\^_`{|}~-]+', "", text)
    
    def emoji_handeling(self,text):
        txt=emoji.demojize(text)
        txt=txt.replace(':',' ')
        txt=txt.replace('_',' ')
        txt=txt.split('_')
        return ''.join(txt)
    
    def call_all_func(self,X):
        X=self.remove_urls(X)
        X=self.remove_mentions(X)
        X=self.emoji_handeling(X)
        X=self.remove_punct(X)
        # X=self.remove_non_ascii(X)

        return X



    

