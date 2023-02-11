import firebase_admin
from firebase_admin import credentials, db 
import os
import json


secret_value = os.environ.get('SERVICEACCOUNTKEY')
secret_value = json.loads(secret_value)



cred = credentials.Certificate(secret_value)
database_url = secret_value['databaseURL']
firebase_admin.initialize_app(cred, {
        'databaseURL': database_url})

ref = db.reference('Dump/')
users_ref = ref.child('users')
users_ref.set({
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
    'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
})