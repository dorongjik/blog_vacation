from django.conf.urls import url
from django.contrib import admin

from django.http.response import HttpResponse

def home(request):
    return HttpResponse("Hello world")

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home), # 여기에 있는 home은 함수 home 임.
]
