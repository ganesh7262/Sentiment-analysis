from transformers import BertTokenizer
import torch
from transformers import BertModel, BertTokenizer
from torch import nn
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
from preprocessor import Preprocessor
processor=Preprocessor()

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



class_names=['negative','neutral','positive']
model=torch.load(r'C:\Users\ganes\OneDrive\Documents\GitHub\Sentment-analysis\BERT sentiment analysis\checkpoint.pth')





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
    return encoded_review['input_ids'].to(device),encoded_review['attention_mask'].to(device)




def final_output():
    input_ids,attention_mask=create_format(review_text)
    output = model(input_ids, attention_mask)
    _, prediction = torch.max(output, dim=1)
    print(f'Review text: {review_text}')
    print(f'Sentiment  : {class_names[prediction]}')


while True:
    review_text=input("Enter the text to determine sentiment: ")
    review_text=processor.call_all_func(review_text)
    final_output()
