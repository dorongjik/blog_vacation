from django.http.response import HttpResponse
from django.conf import settings
from django.template import loader

import requests

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(
        template.render(
            {"site_name" : "대박 투자"},
            request,
        )
    )

def room(request, room_id):
    url = "https://api.zigbang.com/v3/items?detail=true&item_ids=[" + room_id + "]"
    response = requests.get(url)
    return HttpResponse(
        response.content,
    )