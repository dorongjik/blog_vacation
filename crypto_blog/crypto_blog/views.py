from django.http.response import HttpResponse
from django.conf import settings
from django.template import loader
from django.shortcuts import render

import requests

def home(request):
    return render(request,
        "home.html",
        { "site_name":"대박 투자" }, 
    )

def room(request, room_id):
    url = "https://api.zigbang.com/v3/items?detail=true&item_ids=[" + room_id + "]"
    response = requests.get(url)
    return HttpResponse(
        response.content,
    )