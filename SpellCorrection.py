import requests
import json

api_key = '9f972d1ac2de4e168cd4506a2532cd1e'
endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/SpellCheck"

def correct_spellings(text):
    print('test')
    data = {'text': text}
    params = {
        'mkt':'en-us',
        'mode':'proof'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Ocp-Apim-Subscription-Key': api_key,
    }
    response = requests.post(endpoint, headers=headers, params=params, data=data)
    json_response = response.json()
    flagged_tokens = json_response['flaggedTokens']
    for each in flagged_tokens:
        old = each['token']
        new = each['suggestions'][0]['suggestion'] # best suggestion
        text = text.replace(old,new)
    return text 
