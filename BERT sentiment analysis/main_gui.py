from torch import nn
from transformers import BertModel, BertTokenizer
import torch
from transformers import BertTokenizer
from time import sleep
from tkinter import END, messagebox
import tweepy as tw
import pandas as pd
import tkinter as tk
from preprocessor import Preprocessor
UI_FONT = ('Times', 30, 'bold')
# ------------------twitter setup----------#
api_key = "dC5vtwHikzkYPW6SdllG5fmOU"
api_key_secret = "vY3wDvMV8JBBMN9WDVwh7XmtfljPAs7hndvF00GkjA5P7iOpl3"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAAOabQEAAAAAQDoJtk%2FE5Z%2Fp%2BxaMck%2FVofm1o04%3DIxZQW8LNNDU7FGWWYA6hi6anIq7FdLDbY9j7B0MbzwyeL9BuHU"
access_token = "1418895458890571782-m6KTRjewON7dLOHF99DIyL3cHWFuTU"
access_token_secret = "Yhqhc5JRyXcUqkgrrnVQ7c6m769LspiKO0zLcJiijHO6z"
auth = tw.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# -----------------sentiment model setup--------------#
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
processor = Preprocessor()


class SentimentClassifier(nn.Module):

    def __init__(self, n_classes):
        super(SentimentClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(PRE_TRAINED_MODEL_NAME)
        self.drop = nn.Dropout(p=0.3)
        self.out = nn.Linear(self.bert.config.hidden_size, n_classes)

    def forward(self, input_ids, attention_mask):
        _, pooled_output = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=False
        )
        output = self.drop(pooled_output)
        return self.out(output)


class_names = ['negative', 'neutral', 'positive']
model = torch.load(
    r'C:\Users\ganes\OneDrive\Documents\GitHub\Sentment-analysis\BERT sentiment analysis\checkpoint.pth')


MAX_LEN = 160
PRE_TRAINED_MODEL_NAME = 'bert-base-cased'
tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)


def create_format(review_text):
    encoded_review = tokenizer.encode_plus(
        review_text,
        max_length=MAX_LEN,
        add_special_tokens=True,
        return_token_type_ids=False,
        padding='max_length',
        return_attention_mask=True,
        return_tensors='pt',
    )
    return encoded_review['input_ids'].to(device), encoded_review['attention_mask'].to(device)


def final_output(review_text):
    input_ids, attention_mask = create_format(review_text)
    output = model(input_ids, attention_mask)
    _, prediction = torch.max(output, dim=1)
    # print(f'Review text: {review_text}')
    # print(f'Sentiment  : {class_names[prediction]}')
    return f'Review text: {review_text}\nSentiment  : {class_names[prediction]}', prediction


pr = Preprocessor()

# -------------------------------------------functions-----------------------------------------------#


def print_sentiement():
    posi_senti = negative_senti = 0
    to_print = user_search.get()
    
    search_words = to_print
    tweets = tw.Cursor(api.search_tweets,
                       q=search_words,
                       lang="en",
                       ).items(100)
    for tweet in tweets:
        twt_str = tweet.text
        twt_str = pr.call_all_func(twt_str)
        final_out, numeric_senti = final_output(twt_str)
        final_out = '---->' + final_out+'\n'
        out_txt.insert(tk.END, final_out)
        if numeric_senti == 0:
            negative_senti += 1
        elif numeric_senti == 2:
            posi_senti += 1
        else:
            pass
    if posi_senti > negative_senti:
        messagebox.showinfo('General public Sentiment',
                            f'Positive public Opinon\n stats:\n Positive Sentiment: {posi_senti} vs Negative sentiment: {negative_senti}')
    else:
        messagebox.showinfo('General public Sentiment',
                            f'Negative public Opinon\n stats:\n Positive Sentiment: {posi_senti} vs Negative sentiment: {negative_senti}')


def create_out_window():
    global out_txt
    out_txt = tk.Text(width=70, height=20)
    out_txt.delete('1.0',END)
    canvas.create_window(400, 400, window=out_txt)
    print_sentiement()


# ------------------------------------------------------UI-------------------------------------------#


root = tk.Tk()
root.resizable(0, 0)
root.title('Sentiment Classifier')

# ------------image-----------#
bg_img = tk.PhotoImage(
    file=r'C:\Users\ganes\OneDrive\Documents\GitHub\Sentment-analysis\BERT sentiment analysis\images\final.png')


canvas = tk.Canvas(width=800, height=600)
canvas.create_image(400, 300, image=bg_img)
canvas.create_text(410, 50, text='Know What People think about..',
                   font=UI_FONT, fill='white')


# -------get_input-----#

user_search = tk.Entry(width=40)
user_search.focus()
# input_text = canvas.create_text(200, 120, text='Enter the Entity: ', font=(
#     'MS Serif', 20, 'bold'), fill='white')
canvas.create_window(370, 120, window=user_search)
canvas.grid()

search_button = tk.Button(text='Search', command=create_out_window)
search_button.place(x=500, y=107)


root.mainloop()
