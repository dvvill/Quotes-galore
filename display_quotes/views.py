from django.shortcuts import render
from django.views.generic import TemplateView


#Function for context template to display API response data (quotes.html)
class GetQuotes(TemplateView):
    template_name = 'quotes.html'
    def get_context_data(self, *args, **kwargs):
        pass 


