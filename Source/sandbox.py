import requests
import json
import functions
import nltk
nltk.download('punkt')
from nltk import sent_tokenize

tweet, link = functions.NewsLooper2()
print(tweet)
print(link)
text = sent_tokenize(tweet)[:5]
text = ' '.join(text)
count = 0

print(f'{text}, with link {link}')