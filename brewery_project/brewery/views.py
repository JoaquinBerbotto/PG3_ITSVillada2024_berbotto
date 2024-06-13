from django.shortcuts import render
import requests

def index(request):
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.get(url)
    breweries = response.json()
    return render(request, 'index.html', {'breweries': breweries})
