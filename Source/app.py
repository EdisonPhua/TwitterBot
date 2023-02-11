import requests
import json
import functions
import nltk
nltk.download('punkt')
from nltk import sent_tokenize

url = "https://api.twitter.com/2/"

headers = {
    "Authorization": f"Bearer { functions.database_retriever(data='bot_token')['Access_Token'] }"
}
tweet, link = functions.NewsLooper()

text = sent_tokenize(tweet)[:5]
text = ' '.join(text)
count = 0
payload = {
    "text": f'{text}\n\nFull Article:{link}'
}
response = requests.post( (url + 'tweets'), headers=headers, json=payload)
while True:
    if response.status_code in (200,201):
        print(f"Tweet sent successfully")
        break
    elif response.status_code == 401:
        print(f'Token has expired')
        #Get New Access Token with refresh Token. Note, using header not headers
        header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization" : f"Basic {functions.database_retriever(data='Client')['Basic_Auth']}"}
        data = {
        "grant_type": "refresh_token",
        "refresh_token": functions.database_retriever(data='bot_token')['Refresh_Token']}
        response = requests.post( ( url + 'oauth2/token'), data=data, headers=header)
        token_data = response.json()
        access_token = token_data["access_token"]
        refresh_token = token_data["refresh_token"]     
        functions.update_token(New_Access_token=access_token, New_Refresh_Token=refresh_token)
        print('Updates the tokens')
        headers["Authorization"] = f"Bearer {access_token}"
        response = requests.post( (url + 'tweets'), headers=headers, json=payload)
        continue
    elif response.status_code == 400:
        print(f'Text too long')
        count += 1
        text = sent_tokenize(tweet)[:5-count]
        text = ' '.join(text)
        payload['text'] = f'{text}\n\nFull Article:{link}'
        response = requests.post( (url + 'tweets'), headers=headers, json=payload)
        continue     
    else:
        print(f"Error sending tweet code : {response.status_code}" )
        break

    



