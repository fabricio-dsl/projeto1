from django.contrib import admin
from django.urls import path, include

from apps.home import urls as home_urls 
from apps.noticia import urls as noticia_urls 
from apps.video import urls as video_urls 
from apps.depoimento import urls as depoimento_urls 
from apps.sobre import urls as sobre_urls 

urlpatterns = [
    path('', include(home_urls)),
    path('noticia/', include(noticia_urls)),
    path('video/', include(video_urls)),
    path('depoimento/', include(depoimento_urls)),
    path('sobre/', include(sobre_urls)),
]