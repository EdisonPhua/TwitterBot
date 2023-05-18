import functions
import json
from newsdataapi import NewsDataApiClient
import firebase_admin
from firebase_admin import credentials, db 
import os

secret_value = os.environ.get('SERVICEACCOUNTKEY')
secret_value = json.loads(secret_value)

cred = credentials.Certificate(secret_value)
database_url = secret_value["databaseURL"]
try:
    firebase_admin.initialize_app(cred, {
        'databaseURL': database_url})
except ValueError:
    pass 
ref = db.reference('OpenAI/')
users_ref = ref.child('NewsData')
Key = users_ref.get()['API']
api = NewsDataApiClient(apikey=Key)
response = api.news_api( country = 'us,cn,jp,kr,de', category='technology,science', language='en'  )
count = 0
errors = 0

text = response['results'][1]['content']
print(text)

    
    

