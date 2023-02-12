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
ref = db.reference('News/')
News = ref.set()
for Source in News:
            Source_ref = ref.child(Source)
            Source_ref.update({'title': 'Tweeted'})


