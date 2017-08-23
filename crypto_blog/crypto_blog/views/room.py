from django.http.response import HttpResponse
from django.shortcuts import render
import requests

def room(request, room_id):
    url = "https://api.zigbang.com/v3/items?detail=true&item_ids=[" + room_id + "]"
    response = requests.get(url)
    return HttpResponse(
        response.content,
    )