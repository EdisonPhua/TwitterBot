
from newsdataapi import NewsDataApiClient
import firebase_admin
from firebase_admin import credentials, db 
import os


secret_value = os.environ.get('SERVICEACCOUNTKEY')
cred = credentials.Certificate(secret_value)
database_url = secret_value['databaseURL']
firebase_admin.initialize_app(cred, {
        'databaseURL': database_url})

ref = db.reference('Dump/')
ref.set(
    {
        'test':'tester'
    }
)

    

