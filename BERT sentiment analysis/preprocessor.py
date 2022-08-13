import re
import emoji

class Preprocessor:
    
    def remove_URL(self,text):
        return re.sub(r"https?://\S+|www\.\S+", "", text)
    
    def remove_html(self,text):
        html = re.compile(r"<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")
        return re.sub(html, "", text)
    
    def remove_non_ascii(self,text):
        return re.sub(r'[^\x00-\x7f]',r'', text)
    
    def remove_punct(self,text):
        return re.sub(r'[]!"$%&\'()*+,./:;=#@?[\\^_`{|}~-]+', "", text)
    
    def emoji_handling(self,text):
        text = emoji.demojize(text)
        text = text.replace(":"," ")
        text = ' '.join(text.split())
        return text
    
    def call_all_func(self,X):
        X=self.remove_URL(X)
        X=self.remove_html(X)
        X=self.remove_non_ascii(X)
        X=self.remove_punct(X)
        X=self.emoji_handling(X)

        return X



    

