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
while flag == True:
    response = api.news_api( country = 'us,cn,jp,kr,de', category='technology,science', language='en', page=page)  
    for i in range(len(response['results'])):  
        text = response['results'][i]['title']
        if text == None:
            continue
        text = f''' {text} '''
        text = text.split()    
        text = text[:500]
        text = " ".join(text) 
        text = json.dumps(text)
        
        try:
            tldr = functions.generateTLDR(prompt=text) 
        except Exception as e:
            print(f'An error occucured {e}')
            errors += 1
            continue
        
        link = response['results'][i]['link']
        title = response['results'][i]['title']
        date = response['results'][i]['pubDate']  
        count +=1   
        functions.NewsStorer(count=count, date=date,title=title,link=link,content=text,tldr=tldr ) 
        
        if count == 10:
            flag = False
            break

    page = response.get('nextPage',None)
    
    if not page:

        break

print(f'Updated! With {errors} errors!')

    
    

