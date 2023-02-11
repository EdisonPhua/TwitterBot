import functions
import json
from newsdataapi import NewsDataApiClient
import firebase_admin
from firebase_admin import credentials, db 
import os


secret_value = os.environ.get('SERVICEACCOUNTKEY')
cred = credentials.Certificate(secret_value)
database_url = secret_value['databaseURL']
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
while True:
    for i in range(response['totalResults']):    
        try:
            text = response['results'][i]['content']
        except ValueError:
            nextpage = response['nextPage']
            response = api.news_api( country = 'us,cn,jp,kr,de', category='technology,science,business,top', language='en', page=nextpage  )
            continue
        if text == None:
            continue
        text = f''' {text} '''
        text = text.split()    
        text = text[:500]
        text = " ".join(text) 
        text = json.dumps(text)
        tldr = functions.generateTLDR(prompt=text)  
        link = response['results'][i]['link']
        title = response['results'][i]['title']
        date = response['results'][i]['pubDate']  
        count +=1   
        functions.NewsStorer(count=count, date=date,title=title,link=link,content=text,tldr=tldr )   
        if count == 10:
            break
    if count == 10:
        break
print('Updated!')
    
    

