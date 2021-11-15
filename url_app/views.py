from django.shortcuts import render

# Create your views here.
import bitly_api
import requests

def index(request):
    return render(request, 'index.html')


def shortedview(request):

    if(request.method=='POST'): # to get data from form to views
        BITLY_ACCESS_TOKEN ="94720c9bb31daf138af1c199ae5233170fe53d30"
    
        b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
        long_url = request.POST['longurl'] # use this way to fetch data using the name attribute in the input tag
        response = b.shorten(long_url)
        print(response)
        short_url = response.get('url')
        context={'short_url': short_url}

        print(response.get('url'))

        return render(request, 'shortened.html', context)

    return render(request, 'shortened.html')