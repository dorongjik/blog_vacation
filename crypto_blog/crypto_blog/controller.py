from django.http.response import HttpResponse

def home(request):
    return HttpResponse("Hello world")

def room(request, room_id):
    return HttpResponse("room number : " + room_id)