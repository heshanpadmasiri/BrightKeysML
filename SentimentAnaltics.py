import requests
import json

api_key = '<KEY_HERE>'
endpoint = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.1/sentiment'

def get_sentiment(text):
    data = {
        'documents':[
            {
                'language': 'en',
                'id': '1',
                'text': text
            }
        ]
    }
    params = {
        'showSats': True
    }
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': api_key,
    }
    response = requests.post(endpoint, headers=headers, json=data)
    json_response = response.json()
    score = json_response['documents'][0]['score']
    return 1-score # return the sentiment value