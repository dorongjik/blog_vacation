from django.conf.urls import url
from django.contrib import admin

from crypto_blog.controller import home, room # 함수들을 불러옴

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home), # 여기에 있는 home은 함수 home 임.
    url(r'^rooms/(?P<room_id>\d+)/$', room),
]
