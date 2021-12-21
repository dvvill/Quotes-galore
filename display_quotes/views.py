from django.shortcuts import render
from django.views.generic import TemplateView
import requests
# from .services import get_quotes


#Function for context template to display API response data (quotes.html)
class GetQuotes(TemplateView):
    template_name = 'quotes.html'
    def get_context_data(self, *args, **kwargs):
        pass
        # context = {
        #     'quotes' : get_quotes(),
        # }
        # return context
        

# url = 'https://quotes.rest/qod?category=management'
# api_token = "ddXJz0o6BPz2lWEtGOzsrQeF"
# headers = {'content-type': 'application/json',
# 	   'X-TheySaidSo-Api-Secret': format(api_token)}

# response = requests.get(url, headers=headers)
# quotes = response.json()['contents']['quotes'][0]
# print(quotes)


url = "https://theysaidso.p.rapidapi.com/quote/random"

querystring = {"language":"en"}

headers = {
    'x-rapidapi-host': "theysaidso.p.rapidapi.com",
    'x-rapidapi-key': "f4de848189mshec3e8d10ca76422p17f74cjsn6670c70616dc"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

