import requests
import json
import functions
import nltk
nltk.download('punkt')
from nltk import sent_tokenize


tweet, link = functions.NewsLooper()

print(tweet)
print(link)
    