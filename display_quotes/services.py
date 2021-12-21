import requests
import json
import os


# make api requests
url = 'https://quotes.rest/qod?category=management'
api_token = "ddXJz0o6BPz2lWEtGOzsrQeF"
headers = {'content-type': 'application/json',
	   'X-TheySaidSo-Api-Secret': format(api_token)}

# response = requests.get(url, headers=headers)
# quotes = response.json()['contents']['quotes'][0]
# print(quotes)


# Function to send the request and return the response/account info in a python dictionary 
def get_quotes():    
    url = 'https://quotes.rest/qod?category=management'
    response = requests.get(url, headers=headers)
    quotes = response.json()['contents']['quotes'][0]
    quote_list = []
    for i in range(len(quotes['quotes'])):
        quote_list.append(quotes['quotes'][i])
    return quote_list



    