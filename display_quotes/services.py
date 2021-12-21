import requests
import json
import os


# make api requests
api_url_base = 'https://quotes.rest/qod?category=management'
api_token = "ddXJz0o6BPz2lWEtGOzsrQeF"
headers = {'content-type': 'application/json',
	   'X-TheySaidSo-Api-Secret': format(api_token)}

# response = requests.get(url, headers=headers)
# quotes = response.json()['contents']['quotes'][0]
# print(quotes)


# Function to send the request and return the response/account info in a python dictionary 
def get_account_info():

    api_url = '{0}account'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return None


account_info = get_account_info()

if account_info is not None:
    print("Here's your info: ")
    for k, v in account_info['account'].items():
        print('{0}:{1}'.format(k, v))

    else:
        print('[!] Request Failed')