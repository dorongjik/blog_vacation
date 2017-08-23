from django.conf.urls import url
from django.contrib import admin

from crypto_blog.views import * # 함수들을 불러옴.

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name="home"), # 앞의 home은 함수 home, 뒤의 name=home은 template쪽에서 django template("{% url : home %}")을 쓰기 위한 것.
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^about/$', about, name="about"),

    url(r'^policy/terms/$', terms, name="terms"),
    url(r'^policy/privacy/$', privacy, name="privacy"),
    url(r'^policy/disclaimer/$', disclaimer, name="disclaimer"),
]
