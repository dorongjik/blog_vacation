from django.http.response import HttpResponse
import requests

def home(request):
    return HttpResponse("Hello world")

def room(request, room_id):
    url = "https://api.zigbang.com/v3/items?detail=true&item_ids=[" + room_id + "]"
    response = requests.get(url)
    return HttpResponse(
        response.content,
    )