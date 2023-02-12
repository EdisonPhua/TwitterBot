import requests
import json
import functions
import nltk
nltk.download('punkt')
from nltk import sent_tokenize

print('Time to generate new articles')
exec(open("Source/NewsData.py").read())
print('Generated')  

tweet, link = functions.NewsLooper()

text = sent_tokenize(tweet)[:5]
text = ' '.join(text)
count = 0

print(f'{text}, with link {link}')